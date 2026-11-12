"""
MilaEdu Practice Banks & Audio Downloader
Tải trọn bộ 100% câu hỏi, đáp án, giải thích và audio từ các kho đề Aptis
"""

import os
import re
import sys
import json
import time
import requests
import urllib.parse
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DATA_DIR = os.path.join(BASE_DIR, "chrome_profile")
DATA_DIR = os.path.join(BASE_DIR, "data")
QUESTIONS_DIR = os.path.join(DATA_DIR, "questions_json")
AUDIO_DIR = os.path.join(DATA_DIR, "audio")
PRACTICES_DIR = os.path.join(DATA_DIR, "practices")

for d in [QUESTIONS_DIR, AUDIO_DIR, PRACTICES_DIR]:
    os.makedirs(d, exist_ok=True)

PRACTICE_BANKS = [
    {"id": 1, "name": "reading_part_1", "title": "Reading Part 1", "url": "https://milaedu.com/practice/1"},
    {"id": 2, "name": "reading_part_2", "title": "Reading Part 2", "url": "https://milaedu.com/practice/2"},
    {"id": 3, "name": "reading_part_3", "title": "Reading Part 3", "url": "https://milaedu.com/practice/3"},
    {"id": 4, "name": "reading_part_4", "title": "Reading Part 4", "url": "https://milaedu.com/practice/4"},
    {"id": 5, "name": "listening_part_1", "title": "Listening Part 1", "url": "https://milaedu.com/practice/5"},
    {"id": 6, "name": "listening_part_2", "title": "Listening Part 2", "url": "https://milaedu.com/practice/6"},
    {"id": 7, "name": "listening_part_3", "title": "Listening Part 3", "url": "https://milaedu.com/practice/7"},
    {"id": 8, "name": "listening_part_4", "title": "Listening Part 4", "url": "https://milaedu.com/practice/8"},
    {"id": 14, "name": "grammar_vocab_1", "title": "Grammar & Vocab Set 1", "url": "https://milaedu.com/practice/14"},
    {"id": 15, "name": "grammar_vocab_2", "title": "Grammar & Vocab Set 2", "url": "https://milaedu.com/practice/15"},
    {"id": 250, "name": "grammar_vocab_3", "title": "Grammar & Vocab Set 3", "url": "https://milaedu.com/practice/250"},
]

def safe_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name)

def download_audio_file(session, audio_url, filename):
    filepath = os.path.join(AUDIO_DIR, safe_filename(filename))
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        return filepath
    try:
        r = session.get(audio_url, timeout=20)
        if r.status_code == 200 and len(r.content) > 500:
            with open(filepath, "wb") as f:
                f.write(r.content)
            return filepath
    except Exception as e:
        print(f"       [!] Lỗi tải audio {filename}: {e}")
    return None

def extract_and_save_bank(page, item, session):
    url = item["url"]
    name = item["name"]
    title = item["title"]

    print(f"\n[>>>] Đang tải kho bài tập: {title} ({url})")
    try:
        page.goto(url, wait_until="networkidle", timeout=30000)
    except Exception:
        page.goto(url, wait_until="domcontentloaded")
    time.sleep(2)

    content = page.content()

    # Lưu file HTML
    html_file = os.path.join(PRACTICES_DIR, f"{name}.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Chụp ảnh
    screenshot_file = os.path.join(PRACTICES_DIR, f"{name}.png")
    page.screenshot(path=screenshot_file, full_page=False)

    # Trích xuất dữ liệu JSON câu hỏi nhúng trong trang
    m = re.search(r'practiceSession\(JSON\.parse\((.*?)\)\s*,', content, re.DOTALL)
    if not m:
        print(f"  [!] Không tìm thấy practiceSession trong trang {name}")
        return

    raw_str = m.group(1).strip()
    try:
        if raw_str.startswith('"') and raw_str.endswith('"'):
            decoded = json.loads(raw_str)
        elif raw_str.startswith("'") and raw_str.endswith("'"):
            decoded = json.loads('"' + raw_str[1:-1].replace('\\"', '"').replace("'", "\\'") + '"')
        else:
            decoded = json.loads(raw_str)
        questions = json.loads(decoded) if isinstance(decoded, str) else decoded
    except Exception as e:
        print(f"  [!] Lỗi parse JSON cho {name}: {e}")
        return

    print(f"  [V] Trích xuất thành công {len(questions)} câu hỏi cho {title}!")

    # Lưu file JSON câu hỏi chi tiết
    json_path = os.path.join(QUESTIONS_DIR, f"{name}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    # Tải các file Audio nếu có
    audio_count = 0
    for q in questions:
        audio_url = q.get("audio_url")
        audio_path = q.get("audio_path")
        if audio_url:
            audio_name = os.path.basename(audio_path or urllib.parse.urlparse(audio_url).path)
            if not audio_name or not audio_name.endswith(".mp3"):
                audio_name = f"q_{q.get('id', audio_count)}.mp3"
            res = download_audio_file(session, audio_url, audio_name)
            if res:
                audio_count += 1
        
        # Một số câu hỏi có nhiều audio (audio_urls)
        for a_url in q.get("audio_urls", []):
            if a_url:
                a_name = os.path.basename(urllib.parse.urlparse(a_url).path) or f"multi_{int(time.time()*1000)}.mp3"
                if download_audio_file(session, a_url, a_name):
                    audio_count += 1

    if audio_count > 0:
        print(f"  [V] Đã tải thành công {audio_count} file âm thanh (MP3) về thư mục data/audio/!")

def main():
    print("=" * 60)
    print(" BẮT ĐẦU CÀO TOÀN BỘ KHO CÂU HỎI VÀ ÂM THANH (PRACTICE SETS) ")
    print("=" * 60)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            channel="chrome",
            headless=True
        )
        page = context.pages[0] if context.pages else context.new_page()

        # Tạo requests Session với cookie từ browser để tải audio siêu tốc
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        for c in context.cookies():
            session.cookies.set(c["name"], c["value"], domain=c["domain"], path=c["path"])

        for item in PRACTICE_BANKS:
            extract_and_save_bank(page, item, session)
            time.sleep(1)

        print("\n" + "=" * 60)
        print(" [V] TẤT CẢ KHO ĐỀ VÀ ÂM THANH ĐÃ ĐƯỢC TẢI VỀ HOÀN TẤT!")
        print(" - File JSON câu hỏi: data/questions_json/")
        print(" - File Âm thanh: data/audio/")
        print(" - File HTML giao diện: data/practices/")
        print("=" * 60)
        context.close()

if __name__ == "__main__":
    main()

