# Font Guide: LaTeX Beamer → PPTX (Bản chính xác cuối cùng)

## Phát hiện quan trọng

- **Slide PPTX có kích thước 16.02 × 9.01 cm** — gần bằng Beamer 16:9 (16 × 9 cm).
- **Scale ratio = 1.0** → Cỡ chữ trong PPTX đã đúng, KHÔNG CẦN PHÓNG TO.
- **Vấn đề duy nhất:** Adobe thay `Latin Modern` bằng `Arial Black` (bold) và `Arial` (regular).

---

## Bảng ánh xạ Font (Adobe → Latin Modern)

| Font Adobe gán | Cần đổi thành | Ghi chú |
| :--- | :--- | :--- |
| **Arial Black** | **LM Sans 10** | Adobe dùng Arial Black cho chữ đậm của LM Sans |
| **Arial** | **LM Sans 10** | Adobe dùng Arial cho chữ thường của LM Sans |
| **Calibri** | **LM Sans 10** | Một số Frame Title bị nhận diện sai thành Calibri |
| **(inherited)** | **LM Sans 10** | ⚠️ Phải set rõ ràng, không được để inherited |

---

## Chi tiết cỡ chữ từng thành phần (Đã xác minh với cả LaTeX lẫn PPTX)

### Slide 1: Title Slide
| Thành phần | LaTeX command | Size PPTX | Font PPTX → Đổi thành | Bold |
| :--- | :--- | :--- | :--- | :--- |
| Tên hội nghị "43rd HUST..." | `\fontsize{12}{14}` | **12pt** | Arial Black → LM Sans 10 | Yes |
| Tiêu đề bài báo | `\fontsize{18}{21}` | **18pt** | Arial Black → LM Sans 10 | Yes |
| Nhãn "ID:", "Students:", "Supervisor:" | `\small \textbf{}` | **10pt** | Arial Black → LM Sans 10 | Yes |
| Giá trị (S.1.17, tên SV, tên GV) | `\footnotesize` | **9pt** | Arial → LM Sans 10 | No |
| Tên trường, ngày | `\footnotesize` | **9pt** | Arial Black → LM Sans 10 | Yes |

### Slide 2: Problem Statement (Introduction)
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title "Problem Statement" | `\frametitle{}` | **(inherited → 14pt)** | (inherited) → LM Sans 10 |
| Nguồn tham khảo (footnote) | `\fontsize{5pt}{6pt}` | **5pt** | Arial → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

### Slide 3: Solution (Related Work)
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title | `\frametitle{}` | **(inherited → 14pt)** | (inherited) → LM Sans 10 |
| Caption hình | `\scriptsize` (caption) | **8pt** | Arial → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

### Slide 4: Architecture
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title "Architecture" | `\frametitle{}` | **14pt** | Calibri → LM Sans 10 |
| Caption hình | `\scriptsize` (caption) | **8pt** | Arial → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

### Slide 5: Experimental Setup and Results
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title | `\frametitle{}` | **(inherited → 14pt)** | (inherited) → LM Sans 10 |
| ▶ Tam giác đỏ (Bullet cấp 1) | `\textcolor{red}{\small$\blacktriangleright$}` | **10pt, spc=495** | ⚠️ Xem mục "Tam giác đỏ" bên dưới |
| Section header text | `\footnotesize \textbf{}` | **9pt** | Arial Black → LM Sans 10 |
| Bullet items | `\footnotesize` | **9pt** | Arial → LM Sans 10 |
| Table header (Model, Cov, ...) | `\tiny \textbf{}` | **6pt** | Arial Black → LM Sans 10 |
| Table body | `\tiny` | **6pt** | Arial → LM Sans 10 |
| Table caption | `\tiny` | **6pt** | Arial → LM Sans 10 |
| Nguồn tham khảo | `\fontsize{5pt}{6pt}` | **5pt** | Arial → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

### Slide 6: Case Study
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title | `\frametitle{}` | **(inherited → 14pt)** | (inherited) → LM Sans 10 |
| Paper title box | `\scriptsize \textbf{}` | **8pt** | Arial Black → LM Sans 10 |
| Abstract box | `\tiny` | **6pt** | Arial → LM Sans 10 |
| Column header "Baseline/Ours" | `\scriptsize \textbf{}` | **8pt** | Arial Black → LM Sans 10 |
| Column body text | `\tiny` | **6pt** | Arial → LM Sans 10 |
| Citation markers [3755653] | `\tiny \textbf{}` | **6pt** | Arial Black → LM Sans 10 |
| Nguồn tham khảo | `\fontsize{5pt}{6pt}` | **5pt** | Arial → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

### Slide 7: Conclusions and Future Work
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title | `\frametitle{}` | **(inherited → 14pt)** | (inherited) → LM Sans 10 |
| ▶ Tam giác đỏ (Bullet cấp 1) | `\textcolor{red}{\small$\blacktriangleright$}` | **10pt, spc=495** | ⚠️ Xem mục "Tam giác đỏ" bên dưới |
| Section header bold text | `\textbf{}` | **9pt** | Arial Black → LM Sans 10 |
| Bullet items | `\footnotesize` | **9pt** | Arial → LM Sans 10 |
| "THANK YOU FOR LISTENING!" | `\Large \textbf{}` | **14pt** | Arial Black → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

### Slide 8: References
| Thành phần | LaTeX command | Size PPTX | Font → Đổi thành |
| :--- | :--- | :--- | :--- |
| Frame Title | `\frametitle{}` | **(inherited → 14pt)** | (inherited) → LM Sans 10 |
| Reference text | `\tiny` | **(inherited → ~5pt)** | (inherited) → LM Sans 10 |
| Số trang (góc dưới phải) | `\insertpagenumber` | **~10pt** | ⚠️ Field element → LM Sans 10 |

---

## ⚠️ Xử lý đặc biệt: Tam giác đỏ (▶ blacktriangleright)

### Nguyên nhân bị mất
Adobe convert ký tự toán học `$\blacktriangleright$` (U+25B6 ▶) thành ký tự **"I"** (U+0049) với:
- Font: **Arial**, Size: **10pt**, Color: **FF0000** (đỏ)
- Character spacing: **spc=495** (giãn rộng để trông giống tam giác)

Khi đổi font sang LM Sans 10, ký tự "I" vẫn là "I" nhưng spacing bị ảnh hưởng → tam giác biến mất.

### Cách fix
Trong script Python, cần **thay thế ký tự "I" bằng ký tự Unicode "▶" (U+25B6)** tại các vị trí có:
- Color = `FF0000` (đỏ)
- Character spacing `spc=495`

Hoặc thay thủ công trong Keynote/PPT: chọn ký tự "I" đỏ đó → gõ lại ký tự ▶.

---

## ⚠️ Xử lý đặc biệt: Số trang (Page Number)

### Nguyên nhân vẫn dùng Arial
Adobe render số trang dưới dạng **field element** (`<a:fld type="slidenum">`) — không phải run thông thường (`<a:r>`).
Script `has_text_frame` + `paragraph.runs` không bắt được loại này.

- Vị trí: Góc dưới bên phải, tọa độ **(15.2, 8.3) cm**
- Xuất hiện tại: **Slide 2–8** (7 fields)
- Font gốc: **(inherited từ Slide Master)** → Arial

### Cách fix
Cần quét `<a:fld>` elements trong `txBody` và chèn `<a:latin typeface="LM Sans 10"/>` vào bên trong `<a:rPr>` của field đó.
Đồng thời xóa `spc=-50` (spacing âm) trên số trang.

---

## ⚠️ Xử lý đặc biệt: Chấm tròn xanh (● bullet cấp 2)

### Nguyên nhân bé
Adobe render chấm tròn xanh dưới dạng **paragraph-level bullet** (không phải text run) với:
- Ký tự: `•` (U+2022)
- Font: **Arial** → cần đổi thành **LM Sans 10**
- Size: **buSzPct = 66666** (tức 66.67% cỡ chữ paragraph) → **quá bé**
- Color: **#0000B3** (xanh đậm)

Xuất hiện tại:
- **Slide 5** (Experimental Setup): 4 bullets (Environment, Dataset, Metrics, Baselines)
- **Slide 7** (Conclusions): 3 bullets (Collaborative Framework, Empirical Success, System Expansion)

### Cách fix
- Đổi `buFont typeface` từ `Arial` → `LM Sans 10`
- Tăng `buSzPct val` từ `66666` (66%) → `100000` (100%) để chấm tròn to bằng cỡ chữ

---

## ⚠️ Xử lý đặc biệt: Character Spacing (Nguyên nhân chữ dính)

### Nguyên nhân
Adobe gán **680 giá trị character spacing âm** (`spc < 0`) vào các run để chữ vừa khít với font Arial.
Khi đổi sang LM Sans 10 (metrics khác), các giá trị spacing âm này làm chữ **dính vào nhau**.

### Cách fix
- **Xóa bỏ toàn bộ `spc < 0`** (spacing âm) → LM Sans 10 tự giãn cách tự nhiên.
- **Giữ nguyên `spc > 0`** (spacing dương) → Đặc biệt là `spc=495` của tam giác đỏ.

---

## Mã màu chuẩn HUST (từ beamerthemeHUST.sty)

| Tên | Hex | Sử dụng |
| :--- | :--- | :--- |
| `hustprimary` (blue mode) | `#005A8C` | Tiêu đề, nhãn, viền |
| Đỏ hội nghị | `#D90000` | Dòng "43rd HUST..." |
| Đỏ bullet / tam giác | `#FF0000` | Icon ▶ cấp 1 |
| Xanh bullet | `blue!70!black` | Icon • cấp 2 |

---

## Quy tắc đổi font trong script (Bản cuối cùng)

1. Tìm tất cả runs có `font.name` = `Arial Black`, `Arial`, hoặc `Calibri` → Đổi thành `LM Sans 10`.
2. Tìm tất cả runs có `font.name` = `None` (inherited) → **Set rõ ràng** thành `LM Sans 10`.
3. Đổi font trong **Slide Master**, **Slide Layout**, và **Theme** → `LM Sans 10`.
4. **KHÔNG thay đổi cỡ chữ** (`font.size`) — Adobe đã gán đúng rồi.
5. **KHÔNG thay đổi bold** — Adobe đã gán đúng rồi.
6. **Xóa character spacing âm** (`spc < 0`) — Nguyên nhân chữ dính.
7. **Giữ nguyên character spacing dương** (`spc > 0`) — Đặc biệt `spc=495` của tam giác.
8. **Thay ký tự "I" (U+0049) bằng "▶" (U+25B6)** tại các run có color `FF0000` và `spc=495`.
9. **Tăng kích thước chấm tròn xanh** (`buSzPct`) từ `66666` lên `100000` và đổi `buFont` sang `LM Sans 10`.
