import os
import json
import re

DATA_DIR = r"d:\CODE\Aptis\data"
QUESTIONS_DIR = os.path.join(DATA_DIR, "questions_json")
AUDIO_DIR = os.path.join(DATA_DIR, "audio")
PROCESSED_FILE = os.path.join(DATA_DIR, "all_questions_processed.json")

# Map of section keys to files and display names
SECTIONS = [
    {
        "id": "listening_1",
        "skill": "listening",
        "part": 1,
        "title": "Listening Part 1 (Nghe hiểu thông điệp ngắn)",
        "icon": "headphones",
        "file": "listening_part_1.json",
        "desc": "194 câu hỏi trắc nghiệm kèm audio phát ngôn và giải thích chi tiết."
    },
    {
        "id": "listening_2",
        "skill": "listening",
        "part": 2,
        "title": "Listening Part 2 (Ghép ý kiến 4 người nói)",
        "icon": "users",
        "file": "listening_part_2.json",
        "desc": "16 bộ đề, nghe 4 người nói ngắn và nối đúng nhận định."
    },
    {
        "id": "listening_3",
        "skill": "listening",
        "part": 3,
        "title": "Listening Part 3 (Hội thoại thảo luận 2 người)",
        "icon": "message-circle",
        "file": "listening_part_3.json",
        "desc": "16 bộ đề, nghe hội thoại giữa người nam và người nữ rồi chọn quan điểm."
    },
    {
        "id": "listening_4",
        "skill": "listening",
        "part": 4,
        "title": "Listening Part 4 (Độc thoại dài)",
        "icon": "mic",
        "file": "listening_part_4.json",
        "desc": "30 đề nghe độc thoại dài (bản tin, bài giảng) và trả lời 2 câu hỏi."
    },
    {
        "id": "reading_1",
        "skill": "reading",
        "part": 1,
        "title": "Reading Part 1 (Điền từ hoàn thành email)",
        "icon": "book-open",
        "file": "reading_part_1.json",
        "desc": "Các đoạn văn ngắn/email chứa chỗ trống cần chọn từ thích hợp."
    },
    {
        "id": "reading_2",
        "skill": "reading",
        "part": 2,
        "title": "Reading Part 2 (Sắp xếp trật tự câu văn)",
        "icon": "arrow-down-up",
        "file": "reading_part_2.json",
        "desc": "Các câu văn bị đảo trật tự, nhiệm vụ sắp xếp lại thành câu chuyện logic."
    },
    {
        "id": "reading_3",
        "skill": "reading",
        "part": 3,
        "title": "Reading Part 3 (Đọc ghép thông tin 4 người)",
        "icon": "file-text",
        "file": "reading_part_3.json",
        "desc": "Đọc 4 đoạn văn của 4 người khác nhau và trả lời câu hỏi ai đã làm gì."
    },
    {
        "id": "reading_4",
        "skill": "reading",
        "part": 4,
        "title": "Reading Part 4 (Nối tiêu đề đoạn văn)",
        "icon": "heading",
        "file": "reading_part_4.json",
        "desc": "Đọc bài viết dài 7 đoạn văn và nối đúng tiêu đề tương ứng cho mỗi đoạn."
    },
    {
        "id": "grammar_1",
        "skill": "grammar",
        "part": 1,
        "title": "Grammar & Vocabulary - Đề 1",
        "icon": "spell-check",
        "file": "grammar_vocab_1.json",
        "desc": "30 câu hỏi trắc nghiệm ngữ pháp & từ vựng thông dụng Aptis."
    },
    {
        "id": "grammar_2",
        "skill": "grammar",
        "part": 2,
        "title": "Grammar & Vocabulary - Đề 2",
        "icon": "spell-check",
        "file": "grammar_vocab_2.json",
        "desc": "30 câu hỏi trắc nghiệm ngữ pháp & từ vựng trọng tâm Aptis."
    },
    {
        "id": "grammar_3",
        "skill": "grammar",
        "part": 3,
        "title": "Grammar & Vocabulary - Đề 3",
        "icon": "spell-check",
        "file": "grammar_vocab_3.json",
        "desc": "30 câu hỏi trắc nghiệm ngữ pháp & từ vựng nâng cao Aptis."
    }
]

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<.*?>', '', text)
    return text.strip()

processed_db = {
    "sections": [],
    "questions_by_section": {}
}

for sec in SECTIONS:
    fpath = os.path.join(QUESTIONS_DIR, sec["file"])
    if not os.path.exists(fpath):
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        raw_questions = json.load(f)

    sec_copy = {k: v for k, v in sec.items() if k != "file"}
    sec_copy["total_questions"] = len(raw_questions)
    processed_db["sections"].append(sec_copy)

    formatted_q_list = []
    for idx, q in enumerate(raw_questions, 1):
        m = q.get("metadata", {})
        
        # Audio filename resolution
        audio_filename = None
        if q.get("audio_path"):
            audio_filename = os.path.basename(q["audio_path"])
        elif q.get("audio_url"):
            audio_filename = os.path.basename(q["audio_url"].split("?")[0])

        # Verify if audio file exists locally
        has_audio = False
        if audio_filename and os.path.exists(os.path.join(AUDIO_DIR, audio_filename)):
            has_audio = True

        # Resolve correct answer & transcript for Listening 1
        correct_answer = m.get("correct_answer")
        choices = m.get("choices") or []
        desc = m.get("description") or ""

        if not correct_answer and choices and desc:
            for c in choices:
                clean_c = c.strip()
                if f"<strong>{clean_c}</strong>" in desc or f">{clean_c}<" in desc:
                    correct_answer = clean_c
                    break
            if not correct_answer:
                for c in choices:
                    if c.lower() in desc.lower():
                        correct_answer = c
                        break

        # Grammar options
        options = m.get("options") or []
        if options and not choices:
            choices = [opt.get("text", "") if isinstance(opt, dict) else str(opt) for opt in options]

        item = {
            "id": q.get("id", idx),
            "number": idx,
            "skill": sec["skill"],
            "part": sec["part"],
            "type": q.get("type", "mcq"),
            "stem": q.get("stem") or q.get("title") or f"Câu hỏi {idx}",
            "choices": choices,
            "correct_answer": correct_answer,
            "has_audio": has_audio,
            "audio_file": audio_filename if has_audio else None,
            "description": desc,
            "raw_metadata": m
        }
        formatted_q_list.append(item)

    processed_db["questions_by_section"][sec["id"]] = formatted_q_list

with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
    json.dump(processed_db, f, ensure_ascii=False, indent=2)

print(f"Processed {len(processed_db['sections'])} sections and saved to {PROCESSED_FILE}!")
for s in processed_db["sections"]:
    print(f"  - {s['title']}: {s['total_questions']} câu")

