import requests
import json
import re
import os
import time

SPEAKING_SETS = [
    (234, "Đề 1: 2 bố con đá bóng + cưỡi lạc đà - xe ngựa + cố gắng đạt mục tiêu"),
    (235, "Đề 2: Đi bộ qua đường + ngồi xe lăn chơi bóng rổ - chơi thể thao ngoài trời + đi công viên giải trí"),
    (236, "Đề 3 - Phỏng vấn + Đọc sách giấy - đọc sách điện tử + một lần vội vàng"),
    (237, "Đề 4 - Cô gái đi siêu thị + ăn một mình ở nhà - ăn pizza cùng bạn + thể thao mạo hiểm"),
    (238, "Đề 5 - Gia đình ngồi trong ô tô + nghe nhạc trực tiếp - nghe nhạc ở nhà + đọc quyển sách hay"),
    (239, "Đề 6 - cô gái đi xe bus + trẻ em chơi trong nhà - chơi ngoài trời + sử dụng mạng internet"),
    (240, "Đề 7: Bố con nấu ăn + gia đình chơi cờ - cậu bé chơi game + ai đó giúp đỡ bạn"),
    (241, "Đề 8: Cô giáo chơi cùng học sinh + ôm mèo - xem rắn + giúp đỡ người khác"),
    (242, "Đề 9: Xem triển lãm + gia đình ngồi bãi cỏ - cô gái ở ban công + học điều mới"),
    (243, "Đề 10: 3 cậu bé đá bóng + chơi với khỉ - cá voi + đạt được mục tiêu"),
    (244, "Đề 11: Gia đình dùng máy tính + đá bóng - nhảy cao + xem tác phẩm nghệ thuật"),
    (245, "Đề 12: Xem phim ở rạp + ăn trên đường phố - ăn nhà hàng + nhận một món quà"),
    (246, "Đề 13: Mẹ con đọc sách + thuyết trình - làm việc nhóm + kể một lần nhận được quà"),
    (247, "Đề 14: Bố con ăn sáng + trồng rau - trồng hoa + kể một lần đến thăm bạn"),
    (248, "Đề 15: Treo tranh + ăn ở nhà hàng ngoài trời - ăn cùng gia đình - kể một lần đi xa"),
    (253, "Đề 16: Dùng điện thoại + phòng ngủ - camping + gặp người nước ngoài"),
    (254, "Đề 17: Đi bộ trong rừng + Đảo - nhà tuyết + xem thể thao"),
    (255, "Đề 18: chơi game + thành phố - trang trại - thành tựu"),
    (256, "Đề 19: xem thể thao + tàu, máy bay + người gây ấn tượng"),
    (257, "Đề 20: gia đình chơi game + giúp người già - trồng cây + thư giãn"),
]

WRITING_SETS = [
    (204, "Art Club"), (205, "Book club: 1"), (206, "Business club."),
    (207, "Car Club"), (208, "College"), (209, "Community Club"),
    (210, "COMPUTER CLUB"), (211, "Debate club"), (212, "English Club"),
    (213, "FASHION CLUB"), (214, "Film Club"), (215, "Fitness club"),
    (216, "Food Club"), (217, "GARDEN CLUB"), (218, "HEALTH CLUB"),
    (219, "Beautiful Home Club"), (220, "Language Club"), (221, "Museum Club"),
    (222, "Music club"), (223, "Nature Club"), (224, "Outdoor Club"),
    (225, "PHOTOGRAPHY CLUB"), (226, "READING CLUB"), (227, "SCIENCE CLUB"),
    (228, "Social Club"), (229, "Sports club"), (230, "TECHNOLOGY CLUB (phiên bản 1)"),
    (231, "TRAVEL CLUB"), (232, "TV Club"), (233, "Walking club")
]

os.makedirs("data/speaking_sets", exist_ok=True)
os.makedirs("data/writing_sets", exist_ok=True)
os.makedirs("data/images/speaking", exist_ok=True)

import asyncio
from playwright.async_api import async_playwright

async def get_cookies_dict():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=r"D:\CODE\Aptis\chrome_profile",
            headless=True,
            channel="chrome"
        )
        cookies = await context.cookies("https://milaedu.com")
        await context.close()
        return {c['name']: c['value'] for c in cookies}

def download_image(url_path):
    if not url_path:
        return None
    filename = os.path.basename(url_path)
    local_path = os.path.join("data/images/speaking", filename)
    if os.path.exists(local_path):
        return filename
    full_url = f"https://milaedu.com/storage/{url_path}" if not url_path.startswith("http") else url_path
    try:
        r = requests.get(full_url, timeout=10)
        if r.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(r.content)
            return filename
    except Exception as e:
        print(f"Error downloading {full_url}: {e}")
    return filename

def main():
    print("Getting cookies...")
    cookies = asyncio.run(get_cookies_dict())
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Origin": "https://milaedu.com",
    }
    
    s = requests.Session()
    s.cookies.update(cookies)
    
    # 1. Crawl Speaking Sets
    print(f"\n=== CRAWLING {len(SPEAKING_SETS)} SPEAKING SETS ===")
    all_speaking_data = []
    
    for set_id, title in SPEAKING_SETS:
        save_file = f"data/speaking_sets/{set_id}.json"
        if os.path.exists(save_file):
            print(f"[Speaking] Set {set_id} already cached: {title}")
            with open(save_file, encoding="utf-8") as f:
                all_speaking_data.append(json.load(f))
            continue
            
        print(f"[Speaking] Fetching Set {set_id}: {title}...")
        res_page = s.get("https://milaedu.com/mock-test/speaking", headers=headers)
        m_token = re.search(r'name="_token" value="([^"]+)"', res_page.text)
        token = m_token.group(1) if m_token else ""
        
        payload = {"_token": token, "skill": "speaking", "set_id": str(set_id)}
        res_post = s.post("https://milaedu.com/mock-test", data=payload, headers=headers, allow_redirects=True)
        
        m_data = re.search(r'const sectionsData = (\[.*?\]);\s*\n\s*return', res_post.text, re.DOTALL)
        if m_data:
            sections = json.loads(m_data.group(1))
            # Download images
            for sec in sections:
                for q in sec.get("questions", []):
                    meta = q.get("metadata") or {}
                    if meta.get("image_path"):
                        img_fn = download_image(meta["image_path"])
                        meta["local_image"] = img_fn
                    if meta.get("image_paths"):
                        meta["local_images"] = [download_image(ip) for ip in meta["image_paths"]]
                        
            set_record = {
                "set_id": set_id,
                "title": title,
                "skill": "speaking",
                "sections": sections
            }
            with open(save_file, "w", encoding="utf-8") as f:
                json.dump(set_record, f, ensure_ascii=False, indent=2)
            all_speaking_data.append(set_record)
            print(f"  -> Saved Set {set_id} with {len(sections)} sections")
        else:
            print(f"  -> FAILED to parse Set {set_id}!")
        time.sleep(0.5)

    with open("data/all_speaking_sets.json", "w", encoding="utf-8") as f:
        json.dump(all_speaking_data, f, ensure_ascii=False, indent=2)
    print(f"Saved total {len(all_speaking_data)} speaking sets to data/all_speaking_sets.json")

    # 2. Crawl Writing Sets
    print(f"\n=== CRAWLING {len(WRITING_SETS)} WRITING SETS ===")
    all_writing_data = []
    
    for set_id, title in WRITING_SETS:
        save_file = f"data/writing_sets/{set_id}.json"
        if os.path.exists(save_file):
            print(f"[Writing] Set {set_id} already cached: {title}")
            with open(save_file, encoding="utf-8") as f:
                all_writing_data.append(json.load(f))
            continue
            
        print(f"[Writing] Fetching Set {set_id}: {title}...")
        res_page = s.get("https://milaedu.com/mock-test/writing", headers=headers)
        m_token = re.search(r'name="_token" value="([^"]+)"', res_page.text)
        token = m_token.group(1) if m_token else ""
        
        payload = {"_token": token, "skill": "writing", "set_id": str(set_id)}
        res_post = s.post("https://milaedu.com/mock-test", data=payload, headers=headers, allow_redirects=True)
        
        m_data = re.search(r'const sectionsData = (\[.*?\]);\s*\n\s*return', res_post.text, re.DOTALL)
        if m_data:
            sections = json.loads(m_data.group(1))
            set_record = {
                "set_id": set_id,
                "title": title,
                "skill": "writing",
                "sections": sections
            }
            with open(save_file, "w", encoding="utf-8") as f:
                json.dump(set_record, f, ensure_ascii=False, indent=2)
            all_writing_data.append(set_record)
            print(f"  -> Saved Set {set_id} with {len(sections)} sections")
        else:
            print(f"  -> FAILED to parse Set {set_id}!")
        time.sleep(0.5)

    with open("data/all_writing_sets.json", "w", encoding="utf-8") as f:
        json.dump(all_writing_data, f, ensure_ascii=False, indent=2)
    print(f"Saved total {len(all_writing_data)} writing sets to data/all_writing_sets.json")

if __name__ == "__main__":
    main()

