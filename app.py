"""
Aptis Practice Master - Local Learning Server
Máy chủ phục vụ hệ thống ôn luyện Aptis hoàn chỉnh
"""

import os
import sys
import json
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import webbrowser
import threading

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
AUDIO_DIR = os.path.join(DATA_DIR, "audio")
PROCESSED_DB_FILE = os.path.join(DATA_DIR, "all_questions_processed.json")
INSTRUCTIONS_FILE = os.path.join(DATA_DIR, "all_instructions.json")
STATIC_DIR = os.path.join(BASE_DIR, "web")

# Đảm bảo có thư mục web
os.makedirs(STATIC_DIR, exist_ok=True)

# Đọc cơ sở dữ liệu câu hỏi và hướng dẫn
with open(PROCESSED_DB_FILE, "r", encoding="utf-8") as f:
    QUESTIONS_DB = json.load(f)

INSTRUCTIONS_DB = []
if os.path.exists(INSTRUCTIONS_FILE):
    with open(INSTRUCTIONS_FILE, "r", encoding="utf-8") as f:
        INSTRUCTIONS_DB = json.load(f)

class AptisServerHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Range")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # 1. API: Danh sách các Section
        if path == "/api/sections":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(QUESTIONS_DB["sections"], ensure_ascii=False).encode("utf-8"))
            return

        # 2. API: Lấy câu hỏi theo Section ID
        if path.startswith("/api/questions/"):
            sec_id = path.replace("/api/questions/", "").strip("/")
            questions = QUESTIONS_DB["questions_by_section"].get(sec_id, [])
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(questions, ensure_ascii=False).encode("utf-8"))
            return

        # 3. API: Danh sách cẩm nang hướng dẫn
        if path == "/api/instructions":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            # Trả về metadata của các bài hướng dẫn
            meta_list = [{"slug": g["slug"], "title": g["title"]} for g in INSTRUCTIONS_DB]
            self.wfile.write(json.dumps(meta_list, ensure_ascii=False).encode("utf-8"))
            return

        if path.startswith("/api/instructions/"):
            slug = path.replace("/api/instructions/", "").strip("/")
            guide = next((g for g in INSTRUCTIONS_DB if g["slug"] == slug), None)
            if guide:
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(guide, ensure_ascii=False).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
            return

        # 4. Phục vụ file Audio với hỗ trợ HTTP Range Request (Tua nhanh âm thanh)
        if path.startswith("/audio/") or path.startswith("/data/audio/") or path.startswith("/questions/audio/"):
            if path.startswith("/data/audio/"):
                filename = urllib.parse.unquote(path.replace("/data/audio/", ""))
            else:
                filename = urllib.parse.unquote(path.replace("/audio/", ""))
            filepath = os.path.normpath(os.path.join(AUDIO_DIR, filename))

            # Fallback to speakers/ or root audio directory
            if not os.path.exists(filepath):
                bname = os.path.basename(filename)
                alt1 = os.path.join(AUDIO_DIR, "speakers", bname)
                alt2 = os.path.join(AUDIO_DIR, bname)
                if os.path.exists(alt1):
                    filepath = alt1
                elif os.path.exists(alt2):
                    filepath = alt2

            if not os.path.exists(filepath):
                self.send_response(404)
                self.end_headers()
                return

            file_size = os.path.getsize(filepath)
            range_header = self.headers.get("Range")

            if range_header:
                # Parse Range: bytes=start-end
                range_match = range_header.strip().replace("bytes=", "").split("-")
                start = int(range_match[0]) if range_match[0] else 0
                end = int(range_match[1]) if len(range_match) > 1 and range_match[1] else file_size - 1
                length = end - start + 1

                self.send_response(206)
                self.send_header("Content-Type", "audio/mpeg")
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
                self.send_header("Content-Length", str(length))
                self.end_headers()

                with open(filepath, "rb") as f:
                    f.seek(start)
                    self.wfile.write(f.read(length))
            else:
                self.send_response(200)
                self.send_header("Content-Type", "audio/mpeg")
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Length", str(file_size))
                self.end_headers()

                with open(filepath, "rb") as f:
                    self.wfile.write(f.read())
            return

        # 5. Phục vụ file giao diện Web tĩnh (HTML/CSS/JS)
        if path == "/" or path == "":
            path = "/index.html"

        rel_path = path.lstrip("/")
        local_path = os.path.join(STATIC_DIR, rel_path)

        if os.path.exists(local_path) and os.path.isfile(local_path):
            ctype, _ = mimetypes.guess_type(local_path)
            if not ctype:
                ctype = "text/html" if local_path.endswith(".html") else "application/octet-stream"
            
            self.send_response(200)
            self.send_header("Content-Type", f"{ctype}; charset=utf-8")
            self.send_header("Content-Length", str(os.path.getsize(local_path)))
            self.end_headers()

            with open(local_path, "rb") as f:
                self.wfile.write(f.read())
            return

        # Fallback về index.html cho SPA
        index_file = os.path.join(STATIC_DIR, "index.html")
        if os.path.exists(index_file):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(os.path.getsize(index_file)))
            self.end_headers()
            with open(index_file, "rb") as f:
                self.wfile.write(f.read())
            return

        self.send_response(404)
        self.end_headers()

def run_server(port=8080):
    server_address = ("127.0.0.1", port)
    try:
        httpd = HTTPServer(server_address, AptisServerHandler)
    except OSError:
        # Nếu port 8080 bận thì đổi sang 8081
        port = 8081
        server_address = ("127.0.0.1", port)
        httpd = HTTPServer(server_address, AptisServerHandler)

    url = f"http://localhost:{port}"
    print("=" * 65)
    print(" 🚀 APTIS PRACTICE MASTER - HỆ THỐNG ÔN LUYỆN ĐÃ SẴN SÀNG! ")
    print(f" 🌐 Địa chỉ truy cập: {url}")
    print("=" * 65)
    print(" [i] Đang tự động mở trình duyệt web...")
    print(" [i] Bấm Ctrl + C trong Terminal để dừng hệ thống.\n")

    # Mở trình duyệt sau 1 giây
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Đã dừng máy chủ. Chúc bạn ôn luyện thi tốt!")

if __name__ == "__main__":
    run_server()

