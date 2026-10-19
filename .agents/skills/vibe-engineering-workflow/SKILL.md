---
name: vibe-engineering-workflow
description: "Master Smart Router for Vibe Coding: Tự động kiểm tra prerequisites (mattpocock skills), định tuyến (Small/Large x Clear/Unclear), quản lý Branch/PR, Pre-Check Gate, và duy trì CONTEXT.md."
---

# Vibe Engineering Workflow (Master Smart Router)

Skill này là **Bộ Điều Hướng Thông Minh (Smart Router & Engineering Lifecycle)** dành riêng cho Đại Ka khi phát triển phần mềm và Vibe Coding.

## 🎯 Triết lý hành động:
> **"Luôn chọn quy trình nhẹ nhất đủ để triệt tiêu sự mơ hồ và rủi ro triển khai. Bảo mật tuyệt đối, không đoán mò, luôn có điểm tựa Rollback và không để mất não."**

---

## 🔍 Bước 0: Kiểm Tra Điều Kiện Tiên Quyết (Prerequisite Check)

Trước khi bắt đầu, Agent **BẮT BUỘC KIỂM TRA** xem máy đã có bộ `mattpocock/skills` chưa:
- Kiểm tra các skill cốt lõi: `grill-me`, `grill-with-docs`, `tdd`, `to-spec`, `to-tickets`, `wayfinder`, `diagnosing-bugs`, `code-review`, `handoff`.

### ⚠️ Nếu CHƯA CÀI ĐẶT:
Dừng lại ngay và thông báo rõ ràng cho Đại Ka:
> **⚠️ CẢNH BÁO: Bộ công cụ `mattpocock/skills` chưa được cài đặt trên máy!**
> Đại Ka hãy cài đặt trước để kích hoạt đầy đủ sức mạnh workflow bằng cách:
> 1. Clone repo: `git clone https://github.com/mattpocock/skills.git`
> 2. Hoặc yêu cầu em: *"Cài đặt giúp anh repo mattpocock/skills vào Global scope"*.

---

## 🚦 Ma Trận Định Tuyến Công Việc (Router Decision Matrix)

| Nhóm | Phân loại | Hành động & Chiến lược Git/Branch | Workflow thực thi |
| :--- | :--- | :--- | :--- |
| **🟢 Nhóm 1** | **Clear & Small** | **Direct Branch:** Làm trực tiếp trên branch hiện tại, lưu Rollback commit hash | `tdd` (nếu có test seam) hoặc Implement trực tiếp ➜ Pre-check |
| **🟡 Nhóm 2** | **Unclear & Small** | **Feature Branch (tùy chọn):** Làm rõ yêu cầu trước khi code | `grill-with-docs` (hoặc `grill-me`) ➜ `research`/`prototype` ➜ `to-spec` nhẹ ➜ `implement` |
| **🔵 Nhóm 3** | **Clear & Large** | **New Branch + PR:** Tạo `feature/<name>`, xẻ tracer-bullet tickets | `to-spec` ➜ `to-tickets` ➜ `implement` (**1 ticket / 1 fresh session**) ➜ PR review |
| **🟣 Nhóm 4** | **Unclear & Large** | **Wayfinder Branch:** Gỡ nút thắt quyết định kiến trúc trước | `wayfinder` (resolve decision map) ➜ `to-spec` ➜ `to-tickets` ➜ `implement` |

---

## 🌿 Chiến Lược Branching, PR & Rollback An Toàn

1. **Khi nào tạo Branch & PR mới?**
   - **Tạo Branch / PR khi:** Tính năng mới lớn (Large feature), Refactor kiến trúc hệ thống, hoặc thay đổi có nguy cơ breaking change.
   - **Không cần PR khi:** Fix bug nhỏ đã rõ nguyên nhân, tinh chỉnh CSS/UI nhỏ, thêm config/docs nhẹ.
2. **Kế hoạch Rollback Dự Phòng (Zero-Risk Anchor):**
   - Trước khi sửa đổi lớn, luôn lưu lại **Base Commit Hash** vào `CONTEXT.md` (ví dụ: `Rollback Anchor: abc1234`).
   - Nếu xảy ra lỗi nghiêm trọng: Có thể rollback ngay lập tức bằng `git reset --hard <anchor>` hoặc `git revert`.

---

## 📋 Giao Thức Pre-Check 4 Bước (Pre-Check Gate)

Trước khi kết luận **"HOÀN THÀNH / DONE"**, Agent **BẮT BUỘC** tự kiểm tra 4 tiêu chí sau và báo cáo kết quả:

- [ ] **1. Logic Correctness (Đúng Logic):** Đã chạy test hoặc lệnh thực thi thực tế chưa? (Tuyệt đối không đoán mò).
- [ ] **2. Workflow & Code Cleanliness (Sạch sẽ):** Đã dọn sạch `console.log`, biến rác, import thừa và code thừa chưa?
- [ ] **3. Missing Features & Edge Cases (Tính năng & Trường hợp biên):** Có sót điều kiện biên, xử lý lỗi mạng, timeout, hoặc trạng thái loading/empty không?
- [ ] **4. Latent Risks & Security (Rủi ro & Bảo mật):** Có nguy cơ lộ API Key, đụng độ state, memory leak, hoặc vi phạm `.gitignore` không?

---

## 📝 Quy Ước Duy Trì Living `CONTEXT.md`

1. **Vị trí:** Luôn tạo/cập nhật file `CONTEXT.md` tại thư mục gốc của dự án.
2. **Nội dung bắt buộc trong `CONTEXT.md`:**
   - **Current Goal:** Mục tiêu hiện tại của dự án/tính năng.
   - **Decisions & Architecture:** Các quyết định kỹ thuật đã chốt.
   - **What was done:** Những việc vừa hoàn thành (kèm Base Commit Hash để rollback).
   - **Next Steps:** Các bước tiếp theo cần làm.
3. **Thời điểm cập nhật:**
   - Sau khi hoàn thành một mốc quan trọng.
   - Trước khi kết thúc session hoặc trước khi chạy `/handoff`.

---

## 🛡️ Bộ Quy Tắc Bất Biến (Strict Invariants)

1. **Surgical Changes:** Chỉ sửa đúng những dòng code phục vụ yêu cầu.
2. **Strict Verification:** Không báo xong nếu chưa thực sự chạy lệnh/test trên máy.
3. **Single Ticket Scope:** Với task lớn, chỉ làm 1 ticket trên 1 session để bảo vệ context window.
4. **Zero Secrets in Git:** Tuyệt đối không commit file `.env`, service keys, hay token cá nhân.
