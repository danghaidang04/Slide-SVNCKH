# Triết lý Thiết kế Đồ họa (Global Design Guidelines)

Tài liệu này tổng hợp các nguyên tắc và triết lý thiết kế hình ảnh, sơ đồ để sử dụng xuyên suốt trong toàn bộ bài thuyết trình học thuật (Slide HUST). Mục tiêu là duy trì sự nhất quán, tính chuyên nghiệp và đảm bảo mọi hình ảnh đều kết hợp hoàn hảo với form mẫu của slide.

## 1. Kích thước và Tỷ lệ (Dimensions & Aspect Ratio)
*   **Tỷ lệ khung hình lý tưởng (Aspect Ratio):** Các sơ đồ khối, quy trình nên ưu tiên thiết kế theo tỷ lệ **2.35:1** đến **2.4:1** (dạng Ultrawide, tương tự màn hình chiếu rạp).
*   **Lý do:** Khi chèn vào template slide 16:9, tỷ lệ ngang rộng này giúp sơ đồ lấp đầy không gian chiều ngang (`\textwidth`) mà vẫn để lại khoảng trống hợp lý ở mép trên và dưới để nhường không gian cho tiêu đề (Frametitle) và phần trích dẫn (Footnote).

## 2. Bảng màu Học thuật (Academic Color Palette)
*   **Tông màu chủ đạo:** Sử dụng bộ 3 màu **Xanh lam (Blue)**, **Xám (Gray)** và **Trắng (White)**. Đây là các màu mang lại cảm giác công nghệ, hiện đại và tin cậy.
*   **Nguyên tắc và Mã màu (Hex Codes):**
    *   **Màu nhấn (Accent Color):** Dành cho yếu tố quan trọng nhất (mũi tên luồng chính, icon kết quả). Mã màu: Xanh lam học thuật **`#4070A0`**.
    *   **Màu văn bản & Viền nét (Text & Outlines):** Dành cho chữ và nét vẽ icon. Mã màu: Đen/Xám đậm **`#000000`** đến **`#202020`**.
    *   **Màu phụ trợ (Support Color):** Dành cho viền hộp (borders), mũi tên rẽ nhánh phụ. Mã màu: Xám trung tính **`#808080`** đến **`#B0B0C0`**.
    *   **Màu nền (Background):** Dành cho nền hộp (boxes). Mã màu: Trắng **`#FFFFFF`** hoặc Xám sáng **`#F0F0F0`**, **`#E0E0E0`**.
*   **Độ tương phản (Contrast):** Luôn đảm bảo chữ và icon (tối màu) đặt trên nền các khối hộp sáng màu (trắng/xám nhạt) để không bị chói mắt khi chiếu trên màn chiếu lớn.

## 3. Hệ thống Biểu tượng và Hình khối (Iconography & Shapes)
*   **Phong cách Icon:** Ưu tiên sử dụng các bộ biểu tượng có nét vẽ mảnh (**Line-art icon**) kết hợp với mảng tô màu một phần (solid fill) thay vì các icon 3D hoặc đa sắc lộn xộn. 
*   **Hình khối bo góc (Rounded Corners):** Các hộp chứa nội dung (Group boxes), thẻ (cards) nên có đường viền bo góc nhẹ. Điều này tạo cảm giác thiết kế hiện đại, tinh tế và không bị cứng nhắc.
*   **Trực quan hóa bằng Ẩn dụ (Visual Metaphors):** Khuyến khích dùng các hình khối mang tính biểu tượng thay cho các khối vuông thông thường (Ví dụ: Dùng hình "Cái Phễu" để chỉ sự quá tải/thu hẹp, dùng hình "Bánh răng" để chỉ quy trình tự động...).

## 4. Nghệ thuật Chữ (Typography)
*   **Phân cấp kiểu chữ (Hierarchy):**
    *   **Tiêu đề các khối chính:** Viết hoa toàn bộ (ALL CAPS), in đậm (Bold), kích thước lớn nhất.
    *   **Tiêu đề phụ:** Viết hoa chữ cái đầu (Title Case), in đậm, kích thước vừa phải.
    *   **Mô tả ngắn:** Chữ thường, kích thước nhỏ.
*   **Font chữ:** Thống nhất sử dụng font chữ không chân (San-serif) như Arial, Roboto hoặc Inter. Không dùng font chữ có chân (Serif) trong các hình vẽ để tránh gây nhiễu thị giác.

## 5. Bố cục và Luồng thị giác (Layout & Visual Flow)
*   **Hướng đọc tự nhiên:** Tổ chức sơ đồ đi từ Trái sang Phải (Đầu vào $\rightarrow$ Xử lý $\rightarrow$ Đầu ra) hoặc từ Trên xuống Dưới (Nguyên nhân $\rightarrow$ Hệ quả).
*   **Khoảng trắng (White Space/Padding):** Thiết kế phải có "không gian thở". Giữ khoảng cách rộng rãi giữa các hộp (boxes), text và mép ảnh. Tuyệt đối không nhồi nhét đặc chữ hoặc chồng chéo các mũi tên lên nhau.

## 6. Triết lý "Less is More"
Hình ảnh phục vụ mục đích **"Minh họa khái niệm"** chứ không phải **"Ghi chép lý thuyết"**. Cố gắng lược bỏ mọi chi tiết rườm rà. Nếu một đoạn văn có thể thay bằng một từ khóa kèm một icon dễ hiểu, hãy luôn chọn cách dùng icon.
