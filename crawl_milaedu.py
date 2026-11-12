"""
MilaEdu Ultimate Data Crawler
Chương trình cào toàn bộ dữ liệu bài tập, đề thi, âm thanh và từ vựng từ milaedu.com
"""

import os
import re
import sys
import json
import time
import urllib.parse
from lxml import html
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DATA_DIR = os.path.join(BASE_DIR, "chrome_profile")
OUTPUT_DIR = os.path.join(BASE_DIR, "data")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
API_DIR = os.path.join(OUTPUT_DIR, "api_json")

for d in [OUTPUT_DIR, AUDIO_DIR, IMAGES_DIR, API_DIR]:
    os.makedirs(d, exist_ok=True)

PROGRESS_FILE = os.path.join(OUTPUT_DIR, "crawled_urls.json")
ERROR_LOG_FILE = os.path.join(OUTPUT_DIR, "crawl_errors.log")

TARGET_SECTIONS = [
    ("dashboard", "https://milaedu.com/dashboard"),
    ("full_test", "https://milaedu.com/full-test"),
    ("tu_vung", "https://milaedu.com/tu-vung"),
    ("tu_vung_on_tap", "https://milaedu.com/tu-vung/on-tap"),
    ("grammar", "https://milaedu.com/grammar"),
    ("skills_listening", "https://milaedu.com/skills/listening"),
    ("skills_reading", "https://milaedu.com/skills/reading"),
    ("skills_speaking", "https://milaedu.com/skills/speaking"),
    ("skills_writing", "https://milaedu.com/skills/writing"),
    ("history", "https://milaedu.com/history"),
    ("speaking_history", "https://milaedu.com/speaking-history"),
    ("writing_history", "https://milaedu.com/writing-history"),
    ("leaderboard", "https://milaedu.com/leaderboard"),
    ("instructions", "https://milaedu.com/instructions"),
]

# Các URL hệ thống không cần crawl chi tiết
IGNORE_SUBSTRINGS = [
    "/login", "/logout", "/register", "/doi-mat-khau", "/thiet-bi",
    "/forgot-password", "/reset-password", "/san-pham", "/chinh-sach",
    "facebook.com", "zalo.me", "youtube.com", "tiktok.com"
]

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def save_progress(crawled_set):
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(list(crawled_set), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[!] Lỗi lưu tiến độ: {e}")

def log_error(url, error_msg):
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {url} -> {error_msg}\n")

def safe_filename(name):
    # Loại bỏ ký tự đặc biệt khỏi tên file
    return re.sub(r'[\\/*?:"<>|]', '_', name)[:100]

def is_logged_in(page):
    try:
        url = page.url
        if "login" in url or "register" in url:
            return False
        # Kiểm tra các dấu hiệu của tài khoản đã đăng nhập
        content = page.content().lower()
        if any(kw in content for kw in ["đăng xuất", "lịch sử làm bài", "thiết bị của tôi", "chào ", "maihoangxuan"]):
            return True
        if any(sec in url for sec in ["dashboard", "full-test", "skills", "grammar", "tu-vung", "history"]):
            return True
    except Exception:
        pass
    return False

def handle_agreement_and_login(page):
    """Tự động xử lý checkbox điều khoản nếu có"""
    try:
        # Nếu có popup/trang điều khoản
        if page.locator('text="Quy định sử dụng tài khoản"').count() > 0 or page.locator('text="Tôi đã đọc và đồng ý"').count() > 0:
            print("[+] Phát hiện màn hình 'Quy định sử dụng tài khoản' -> Đang tự động xác nhận...")
            checkbox = page.locator('input[type="checkbox"]')
            if checkbox.count() > 0 and not checkbox.first.is_checked():
                checkbox.first.check()
                time.sleep(0.5)
            
            btn_agree = page.locator('button:has-text("Đồng ý và bắt đầu học"), button:has-text("Đồng ý")')
            if btn_agree.count() > 0:
                btn_agree.first.click()
                time.sleep(2)
                print("[+] Đã bấm 'Đồng ý và bắt đầu học'.")
    except Exception as e:
        print(f"[!] Ghi chú khi xử lý điều khoản: {e}")

def setup_network_intercept(page):
    """Tự động bắt tất cả file âm thanh, ảnh bài tập và dữ liệu JSON từ API"""
    def on_response(response):
        try:
            url = response.url
            content_type = response.headers.get("content-type", "").lower()
            
            # Bắt Audio (Rất quan trọng cho Aptis Listening)
            if any(t in content_type for t in ["audio/", "audio/mpeg", "audio/mp3", "audio/wav"]) or any(url.endswith(ext) for ext in [".mp3", ".wav", ".m4a", ".ogg"]):
                audio_name = os.path.basename(urllib.parse.urlparse(url).path)
                if not audio_name or len(audio_name) < 3:
                    audio_name = f"audio_{int(time.time()*1000)}.mp3"
                audio_path = os.path.join(AUDIO_DIR, safe_filename(audio_name))
                if not os.path.exists(audio_path):
                    body = response.body()
                    if body and len(body) > 1000:
                        with open(audio_path, "wb") as f:
                            f.write(body)
                        print(f"       [Audio] Đã tải âm thanh: {audio_name} ({len(body)//1024} KB)")

            # Bắt JSON API bài tập / câu hỏi
            elif "application/json" in content_type and "milaedu.com" in url:
                if any(k in url for k in ["api", "data", "test", "question", "bai-tap", "cau-hoi", "detail"]):
                    path_part = safe_filename(urllib.parse.urlparse(url).path.replace('/', '_'))
                    json_path = os.path.join(API_DIR, f"{path_part}_{int(time.time()*1000)}.json")
                    body = response.body()
                    if body and len(body) > 50:
                        with open(json_path, "wb") as f:
                            f.write(body)
        except Exception:
            pass

    page.on("response", on_response)

def extract_all_links(page, base_section_url):
    """Tìm tất cả các link bài tập và phân trang trên trang hiện tại"""
    discovered = set()
    try:
        # Lấy toàn bộ href từ trang
        hrefs = page.eval_on_selector_all("a[href]", "elements => elements.map(el => el.href)")
        for href in hrefs:
            if not href or not href.startswith("https://milaedu.com"):
                continue
            # Bỏ qua các link hệ thống không cần thiết
            if any(ig in href for ig in IGNORE_SUBSTRINGS):
                continue
            # Bỏ qua các file tĩnh
            if any(href.endswith(ext) for ext in [".css", ".js", ".png", ".jpg", ".svg", ".ico", ".woff", ".woff2"]):
                continue
            
            # Thu thập nếu link thuộc section này hoặc là dạng link bài tập
            if href == base_section_url or href == base_section_url + "/":
                continue
            
            # Link bài tập con thường chứa prefix của section hoặc chứa từ khóa
            if href.startswith(base_section_url) or any(k in href for k in ["/skills/", "/bai-tap/", "/test/", "/de-thi/", "/part-"]):
                discovered.add(href)
    except Exception as e:
        print(f"[!] Lỗi khi quét liên kết: {e}")
    return sorted(list(discovered))

def click_interactive_tabs(page):
    """Tự động click qua các Part / Tab bài tập để load hết câu hỏi vào DOM"""
    try:
        # Tìm các nút dạng tab: Part 1, Part 2, Part 3, Part 4, Câu 1, Câu 2...
        tab_selectors = [
            'button:has-text("Part 1")', 'button:has-text("Part 2")',
            'button:has-text("Part 3")', 'button:has-text("Part 4")',
            'button:has-text("Phần 1")', 'button:has-text("Phần 2")',
            'button:has-text("Phần 3")', 'button:has-text("Phần 4")',
            '[role="tab"]'
        ]
        for sel in tab_selectors:
            tabs = page.locator(sel)
            count = tabs.count()
            if count > 0:
                for i in range(count):
                    try:
                        tabs.nth(i).click(timeout=1000)
                        time.sleep(0.5)
                    except Exception:
                        pass
    except Exception:
        pass

def download_media_from_html(page):
    """Tìm và tải các file audio, image có sẵn trong HTML mà chưa tải qua response"""
    try:
        # Tìm thẻ audio
        audio_srcs = page.eval_on_selector_all("audio, source", "elements => elements.map(e => e.src)")
        for src in audio_srcs:
            if src and src.startswith("http") and not any(src.endswith(ext) for ext in [".css", ".js"]):
                name = safe_filename(os.path.basename(urllib.parse.urlparse(src).path) or f"media_{int(time.time())}.mp3")
                dest = os.path.join(AUDIO_DIR, name)
                if not os.path.exists(dest):
                    try:
                        import requests
                        r = requests.get(src, timeout=10)
                        if r.status_code == 200 and len(r.content) > 500:
                            with open(dest, "wb") as f:
                                f.write(r.content)
                            print(f"       [Audio Tag] Tải thành công: {name}")
                    except Exception:
                        pass
    except Exception:
        pass

def crawl_page(page, url, save_dir, filename_prefix="detail"):
    """Tải và lưu chi tiết 1 trang bài tập"""
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=25000)
        time.sleep(1.5)

        # Xử lý các tab/part con nếu có
        click_interactive_tabs(page)
        time.sleep(0.5)

        # Lưu file HTML
        html_content = page.content()
        html_file = os.path.join(save_dir, f"{filename_prefix}.html")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Tải media bổ sung từ HTML
        download_media_from_html(page)

        # Chụp ảnh minh chứng
        screenshot_file = os.path.join(save_dir, f"{filename_prefix}.png")
        try:
            page.screenshot(path=screenshot_file, full_page=False)
        except Exception:
            pass

        return True
    except Exception as e:
        log_error(url, str(e))
        print(f"       [!] Lỗi tải {url}: {e}")
        return False

def run():
    crawled_urls = load_progress()
    print("=" * 60)
    print(" MILAEDU AUTO-CRAWLER: HỆ THỐNG THU THẬP DỮ LIỆU TỰ ĐỘNG ")
    print(f" [*] Đã tải trước đó: {len(crawled_urls)} liên kết")
    print("=" * 60)

    with sync_playwright() as p:
        print("[*] Đang khởi động trình duyệt Chrome (profile cố định chống khóa thiết bị)...")
        context = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            channel="chrome",
            headless=False,
            viewport={"width": 1366, "height": 850}
        )
        page = context.pages[0] if context.pages else context.new_page()
        setup_network_intercept(page)

        print("[*] Đang mở MilaEdu...")
        page.goto("https://milaedu.com/dashboard", wait_until="domcontentloaded")
        time.sleep(2)

        # Xử lý đăng nhập / điều khoản nếu chưa đăng nhập
        if not is_logged_in(page):
            print("\n" + "!" * 60)
            print(" [CHỜ ĐĂNG NHẬP] Trình duyệt Chrome đã mở trên màn hình của bạn.")
            print(" - Vui lòng nhập mật khẩu mới và mã OTP từ Gmail (nếu có yêu cầu).")
            print(" - Bot sẽ tự động tích ô điều khoản và tự bắt đầu ngay khi vào được.")
            print("!" * 60 + "\n")

            start_wait = time.time()
            while not is_logged_in(page):
                handle_agreement_and_login(page)
                time.sleep(2)
                if time.time() - start_wait > 600: # Chờ tối đa 10 phút
                    print("[X] Hết thời gian chờ (10 phút). Hãy chạy lại khi bạn sẵn sàng.")
                    context.close()
                    return

        print("\n" + "=" * 60)
        print(" [V] XÁC THỰC THÀNH CÔNG! BẮT ĐẦU CÀO TOÀN BỘ DỮ LIỆU...")
        print("=" * 60 + "\n")

        # 1. Duyệt qua từng Section chính
        for section_name, section_url in TARGET_SECTIONS:
            section_dir = os.path.join(OUTPUT_DIR, section_name)
            os.makedirs(section_dir, exist_ok=True)

            print(f"\n[>>>] ĐANG THU THẬP DANH MỤC: {section_name.upper()}")
            print(f"      URL: {section_url}")

            # Lưu trang chính của danh mục
            if section_url not in crawled_urls:
                crawl_page(page, section_url, section_dir, filename_prefix="index")
                crawled_urls.add(section_url)
                save_progress(crawled_urls)

            # Thu thập tất cả các bài tập / liên kết con
            sub_links = extract_all_links(page, section_url)

            # Kiểm tra phân trang (Trang 2, 3...) nếu có
            try:
                page_links = page.eval_on_selector_all("a[href*='page=']", "elements => elements.map(e => e.href)")
                for pl in set(page_links):
                    if pl not in crawled_urls:
                        print(f"      [Phân trang] Đang quét: {pl}")
                        page.goto(pl, wait_until="domcontentloaded", timeout=20000)
                        time.sleep(1)
                        sub_links.extend(extract_all_links(page, section_url))
            except Exception:
                pass

            unique_sub_links = sorted(list(set(sub_links)))
            print(f"      -> Tìm thấy tổng cộng {len(unique_sub_links)} bài tập / liên kết chi tiết.")

            # Crawl từng bài tập con
            for idx, sub_url in enumerate(unique_sub_links):
                if sub_url in crawled_urls:
                    print(f"      [{idx+1}/{len(unique_sub_links)}] (Đã tải bỏ qua) {sub_url}")
                    continue

                slug = safe_filename(urllib.parse.urlparse(sub_url).path.strip('/').replace('/', '_') or f"item_{idx+1}")
                print(f"      [{idx+1}/{len(unique_sub_links)}] Đang tải chi tiết: {sub_url}")
                
                success = crawl_page(page, sub_url, section_dir, filename_prefix=slug)
                if success:
                    crawled_urls.add(sub_url)
                    save_progress(crawled_urls)
                time.sleep(1) # Giãn cách nhẹ tránh overload

        print("\n" + "=" * 60)
        print(" [V] HOÀN TẤT CRAWL 100% TOÀN BỘ HỆ THỐNG MILAEDU!")
        print(f" - Tổng liên kết đã tải: {len(crawled_urls)}")
        print(f" - Thư mục HTML/Ảnh: {OUTPUT_DIR}")
        print(f" - Thư mục Âm thanh (Audio): {AUDIO_DIR}")
        print(f" - Thư mục Dữ liệu API JSON: {API_DIR}")
        print("=" * 60)
        context.close()

if __name__ == "__main__":
    run()
