# etsy-title-tag – Claude Skill viết Title, Tag & Description cho Etsy

Skill cho [Claude Code](https://claude.com/claude-code) / Claude app giúp viết và kiểm tra **tiêu đề, 13 tag, category/attribute và mô tả** cho listing Etsy, bám theo tài liệu chính thức của Etsy (Seller Handbook + Help Center, cập nhật 04/2026).

## Skill làm được gì

- **Soi ảnh sản phẩm**: nhận diện kỹ thuật (kể cả kỹ thuật phụ như applique, patch…), phong cách, cách khách đặt hàng, từ đồng nghĩa.
- **Xét mùa vụ theo thiết kế** (làm riêng cho dịp / theo mùa / quanh năm) và cảnh báo khi đăng muộn.
- **Nghiên cứu từ khóa** theo 7 nhóm Etsy gợi ý; loại từ khóa sai trọng tâm, có bản quyền/thương hiệu, hoặc màu phôi.
- **2–3 phương án** cho mỗi phần (title, tag, description), mỗi phương án có lý do, có ⭐ đề xuất và nằm trong khối code để bấm Copy.
- **Checklist bắt buộc**: title ≤ 140 ký tự và < 15 từ, đúng 13 tag ≤ 20 ký tự, không lặp, không bịa thông tin… Mọi thứ được đếm bằng công cụ, không ước lượng.
- **Phân tích listing đối thủ**: lấy từ khóa tốt, chỉ ra lỗi rule, không chép cách viết.
- **Bảng số liệu từ khóa có dẫn nguồn** nếu có kết nối YTrends (tùy chọn).

## Cài đặt

**Claude Code (macOS / Linux):**

```bash
git clone https://github.com/tuan1523/etsy-title-tag.git ~/.claude/skills/etsy-title-tag
```

**Windows (PowerShell):**

```powershell
git clone https://github.com/tuan1523/etsy-title-tag.git $HOME\.claude\skills\etsy-title-tag
```

**Claude.ai / Claude Desktop:** tải repo dưới dạng ZIP, rồi vào *Settings → Capabilities → Skills* để upload.

Cập nhật bản mới:

```bash
git -C ~/.claude/skills/etsy-title-tag pull
```

## Cách dùng

Gõ `/etsy-title-tag` rồi gửi ảnh sản phẩm, hoặc nói tự nhiên, ví dụ: *"Viết title và tag Etsy cho mẫu này"*.

Nên gửi kèm (nếu có): chất liệu, size, khả năng cá nhân hóa, thời gian xử lý, tiêu đề và tag của đối thủ. Skill **không tự bịa** những thông tin này.

## Dữ liệu từ khóa (tùy chọn)

Skill chạy được mà không cần dữ liệu ngoài. Khi đó nó chọn từ khóa theo nguyên tắc long-tail của Etsy.

Nếu Claude có kết nối MCP của [YTrends](https://trends.ytuong.ai), skill sẽ dùng `ytrends_research_keyword` và `ytrends_trend_calendar` để chấm điểm từ khóa và dẫn số liệu. Số liệu YTrends là ước tính trên một phần dữ liệu Etsy, nên chỉ dùng để so sánh tương đối giữa các từ khóa.

## Nguồn

Toàn bộ rule dựa trên tài liệu chính thức của Etsy, danh sách link ở cuối [SKILL.md](SKILL.md).

## Đóng góp

Mọi góp ý, issue và pull request đều được hoan nghênh, nhất là khi Etsy cập nhật hướng dẫn mới.

## License

[MIT](LICENSE)
