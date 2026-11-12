# Aptis Master - Hệ Thống Luyện Thi Aptis Trực Tuyến & Ngoại Tuyến

Hệ thống luyện thi Aptis toàn diện với đầy đủ ngân hàng câu hỏi, âm thanh gốc (243 audio files), đáp án chuẩn 100% cùng lời giải chi tiết và cẩm nang chiến thuật làm bài. Ứng dụng chạy mượt mà cả **Offline trên máy tính** và **Online trên Netlify**.

---

## 🎯 Các tính năng chính

- 🎧 **Listening (Parts 1, 2, 3, 4):** Đầy đủ 243 bài nghe audio MP3, hỗ trợ thanh tua bài nghe (seekbar), chỉnh tốc độ phát (0.8x, 1.0x, 1.2x), đếm số lần nghe và transcript kèm dịch nghĩa.
- 📖 **Reading (Parts 1, 2, 3, 4):** Điền từ đoạn văn, sắp xếp câu văn thành đoạn hoàn chỉnh (kèm nút đổi vị trí ⬆ ⬇), ghép người với ý kiến, ghép tiêu đề đoạn văn.
- ✍️ **Grammar & Vocabulary:** Bộ đề ngữ pháp và từ vựng phong phú, giải thích chi tiết từng câu.
- 💡 **Instant Evaluation & Explanations:** Chấm điểm tức thời, hiển thị ngay đáp án đúng/sai kèm giải thích chi tiết.
- 💾 **Lưu tiến độ học tập (Auto-save):** Tự động ghi nhớ các câu đã làm qua `localStorage`.
- 📚 **Cẩm nang chiến thuật:** 12 bài viết chiến thuật độc quyền từ giáo viên Aptis.

---

## 🚀 Hướng Dẫn Deploy Lên Netlify (Chỉ 1 Phút)

Hệ thống được thiết kế theo kiến trúc **JAMstack tĩnh thuần túy** (HTML5 + Tailwind CSS + Vanilla JS + Static JSON & MP3). Do đó, bạn có thể triển khai lên Netlify hoàn toàn miễn phí và không cần cấu hình build phức tạp:

### Cách 1: Kết nối trực tiếp qua GitHub (Khuyên dùng)
1. Tạo một repository mới trên **GitHub** (ví dụ: `aptis-master` hoặc `aptis-practice`).
2. Push toàn bộ mã nguồn lên repository:
   ```bash
   git remote add origin https://github.com/<tai-khoan-cua-ban>/<ten-repo>.git
   git branch -M main
   git push -u origin main
   ```
3. Đăng nhập vào [Netlify](https://app.netlify.com/):
   - Chọn **Add new site** > **Import an existing project**.
   - Chọn **GitHub** và chọn repo bạn vừa push lên.
   - Các thông số thiết lập:
     - **Base directory:** *(để trống)*
     - **Build command:** *(để trống)*
     - **Publish directory:** `.` (hoặc để trống)
   - Bấm **Deploy site**.
4. Netlify đã cấu hình sẵn file `netlify.toml` tự động tối ưu cache và phân phối byte-range cho audio files. Trang web sẽ sẵn sàng truy cập ngay lập tức!

### Cách 2: Kéo thả thủ công (Netlify Drop)
1. Đăng nhập [Netlify Drop](https://app.netlify.com/drop).
2. Kéo toàn bộ thư mục `Aptis` thả vào giao diện Netlify Drop (lưu ý không cần kéo thư mục `chrome_profile/`).

---

## 💻 Hướng Dẫn Chạy Offline Trên Máy Tính

Không cần kết nối internet hay tài khoản:

- **Cách nhanh nhất:** Nhấp đúp chuột vào file **`Chay_On_Luyen_Aptis.bat`**. Trình duyệt sẽ tự động mở tại `http://localhost:8080`.
- **Dùng dòng lệnh:**
  ```powershell
  python app.py
  ```

---

## 📁 Cấu Trúc Thư Mục

```
Aptis/
├── index.html                     # Giao diện ứng dụng chính (Single Page Application)
├── netlify.toml                   # Cấu hình cache, CORS và byte-range cho Netlify
├── README.md                      # Tài liệu dự án
├── HUONG_DAN_SU_DUNG.md           # Hướng dẫn ôn luyện chi tiết
├── app.py                         # Local server hỗ trợ Range Request cho audio
├── Chay_On_Luyen_Aptis.bat        # Launcher 1-click cho Windows
├── data/
│   ├── all_questions_processed.json  # Toàn bộ câu hỏi, đáp án, transcript
│   ├── all_instructions.json     # Cẩm nang 12 chiến thuật ôn thi
│   ├── APTIS_TONG_HOP_DE_VA_DAP_AN.md # File markdown tổng hợp đề và giải
│   └── audio/                     # 243 file audio MP3 các bài nghe Aptis
```
