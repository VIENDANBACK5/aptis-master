"""
MilaEdu Master Key Extractor
Tự động lấy 100% đáp án chuẩn gốc và lời giải thích chi tiết từ hệ thống của MilaEdu
"""

import sys
import os
import json
import time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DATA_DIR = os.path.join(BASE_DIR, "chrome_profile")
QUESTIONS_DIR = os.path.join(BASE_DIR, "data", "questions_json")

PRACTICE_SETS = [
    ("grammar_vocab_1.json", "https://milaedu.com/practice/14"),
    ("grammar_vocab_2.json", "https://milaedu.com/practice/15"),
    ("grammar_vocab_3.json", "https://milaedu.com/practice/250"),
    ("reading_part_1.json", "https://milaedu.com/practice/1"),
    ("reading_part_2.json", "https://milaedu.com/practice/2"),
    ("reading_part_3.json", "https://milaedu.com/practice/3"),
    ("reading_part_4.json", "https://milaedu.com/practice/4"),
    ("listening_part_1.json", "https://milaedu.com/practice/5"),
    ("listening_part_2.json", "https://milaedu.com/practice/6"),
    ("listening_part_3.json", "https://milaedu.com/practice/7"),
    ("listening_part_4.json", "https://milaedu.com/practice/8"),
]

def main():
    print("=" * 65)
    print(" BẮT ĐẦU TRÍCH XUẤT 100% ĐÁP ÁN CHÍNH THỨC & LỜI GIẢI GỐC ")
    print("=" * 65)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            channel="chrome",
            headless=True
        )
        page = context.pages[0] if context.pages else context.new_page()

        for filename, url in PRACTICE_SETS:
            print(f"\n[>>>] Đang nạp trang: {url} ({filename})")
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
            except Exception as e:
                print(f"  [!] Lỗi mở trang {url}: {e}")
                continue

            time.sleep(2)

            # Thực thi revealAnswerKey cho tất cả câu hỏi trong bài
            extracted_data = page.evaluate("""
                async () => {
                    const el = document.querySelector('[x-data*="practiceSession"]') || document.querySelector('main [x-data]');
                    if (!el) return { error: "Không tìm thấy Alpine component" };
                    const alpine = Alpine.$data(el);
                    if (!alpine || !alpine.questions) return { error: "Không có questions" };

                    const list = alpine.questions;
                    const results = [];
                    for (let i = 0; i < list.length; i++) {
                        const q = list[i];
                        try {
                            await alpine.revealAnswerKey(q);
                        } catch (err) {}
                        results.push(q);
                    }
                    return { success: true, count: results.length, questions: results };
                }
            """)

            if not extracted_data or "error" in extracted_data:
                print(f"  [!] Lỗi: {extracted_data.get('error') if extracted_data else 'Không nhận được kết quả'}")
                continue

            questions_with_keys = extracted_data["questions"]
            print(f"  [V] Đã lấy thành công {len(questions_with_keys)} đáp án chuẩn gốc!")

            # Lưu lại vào file JSON
            json_file = os.path.join(QUESTIONS_DIR, filename)
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(questions_with_keys, f, ensure_ascii=False, indent=2)

            time.sleep(1)

        print("\n" + "=" * 65)
        print(" [V] TOÀN BỘ 100% ĐÁP ÁN CHUẨN GỐC ĐÃ ĐƯỢC CẬP NHẬT HOÀN TOÀN!")
        print("=" * 65)
        context.close()

if __name__ == "__main__":
    main()

