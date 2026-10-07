---
name: etsy-title-tag
description: Viết và kiểm tra tiêu đề (title), 13 tag, category/attribute và mô tả (description) cho listing Etsy theo tài liệu chính thức của Etsy (Seller Handbook + Help Center, cập nhật 04/2026), có xét mùa vụ theo thiết kế và có thể kết hợp dữ liệu từ khóa YTrends. Mỗi phần đưa ra 2–3 phương án kèm lý do và bảng số liệu từ khóa có dẫn nguồn, sẵn nút copy. Dùng khi cần viết mới, tối ưu lại, review listing Etsy, hoặc so sánh với tiêu đề/tag của listing đối thủ.
---

# Etsy Title, Tag & Description

## 0. Nguyên tắc nền

1. **Etsy là luật, YTrends là công cụ chọn lựa.**
   - Tài liệu chính thức của Etsy quyết định điều gì được và không được làm.
   - Dữ liệu YTrends (nếu có) chỉ dùng để chọn giữa các từ khóa **đã đúng với sản phẩm**.
   - Khi hai nguồn mâu thuẫn, rule của Etsy thắng.
2. **Viết cho người mua, không viết cho máy** (“keep a buyer in mind, not a computer”).
3. **Không bịa thông tin.**
   - Chỉ dùng chất liệu, size, form, thời gian xử lý, khả năng cá nhân hóa… khi người dùng cung cấp.
   - Không có thì **bỏ hẳn**: không đoán, không để chỗ trống kiểu `[Material]`.
   - Etsy cấm mô tả sai sự thật (House Rules – mislabeling).
4. **Mặc định không ghi màu của phôi sản phẩm** (màu áo, màu cốc…).
   - Lý do: nhiều shop bán một thiết kế trên nhiều màu phôi. Ghi một màu sẽ sai với các biến thể còn lại.
   - Màu **của thiết kế** (màu chỉ thêu, màu họa tiết) vẫn được mô tả, vì nó không đổi giữa các biến thể.
   - Chỉ ghi màu phôi khi người dùng nói rõ sản phẩm chỉ có một màu.

### Etsy Search hoạt động thế nào (lý do đằng sau các rule)
- Search có 2 pha: **query matching** (gom listing khớp từ khóa) và **ranking** (xếp hạng).
- Khi matching, Etsy xem **toàn bộ listing**: title, tag, attribute, category, description, ảnh đầu tiên, review.
  → Một từ khóa có ở bất kỳ nơi nào trong số đó là đã được match. Tiêu đề không cần gánh hết từ khóa.
- Từ khóa **khớp chính xác** với truy vấn có thể được xếp hạng cao hơn.
- **Vị trí của từ trong tiêu đề và thứ tự tag KHÔNG ảnh hưởng thứ hạng.** Thứ tự chỉ ảnh hưởng cách người mua và Google đọc.
- **Tỷ lệ chuyển đổi là yếu tố xếp hạng.** Từ khóa lệch trọng tâm sản phẩm khiến người mua bấm vào rồi bỏ đi, làm hại thứ hạng chung.
- **Listing mới** được ưu tiên tạm thời, kéo dài từ vài giờ đến vài ngày, để Etsy thu thập dữ liệu (*How Etsy Search Works*).

## 1. Thu thập đầu vào

| Loại | Thông tin |
|---|---|
| **Bắt buộc** (lấy từ ảnh hoặc người dùng) | Sản phẩm là gì; kỹ thuật (thêu, in, khắc…); các thành phần thiết kế và đâu là **thành phần chính**; màu của thiết kế; câu chữ trên sản phẩm (nếu có) |
| **Tùy chọn** (chỉ dùng khi người dùng cung cấp) | Màu phôi (chỉ khi bán đúng 1 màu), chất liệu, dải size, form, cá nhân hóa, thời gian xử lý, nơi gửi hàng, hướng dẫn bảo quản |
| **Tùy chọn – đối thủ** | Tiêu đề và tag của listing đối thủ cùng mẫu (xử lý ở bước 3d) |

Nếu thiếu thông tin tùy chọn: viết bản không có thông tin đó. Ở cuối output, ghi **một dòng** liệt kê thông tin nào nếu được bổ sung sẽ làm listing tốt hơn.

### Soi ảnh (bắt buộc, làm trước bước 3)
Ghi ra đủ 4 mục sau ở phần "Phân tích nhanh". Mỗi mục đều sinh từ khóa ứng viên cho bước 3a.

1. **Mọi kỹ thuật nhìn thấy, kể cả kỹ thuật phụ.** Không dừng ở kỹ thuật chính.
   - Ví dụ: chân dung thêu, nhưng nền caro là **vải đắp** → thêu + applique.
   - Các kỹ thuật hay bị bỏ sót: applique, patch, chenille, puff print, distressed, tie-dye, hand-painted.
   - Nếu không chắc từ ảnh, ghi là "có thể" và hỏi lại người dùng trong Ghi chú.
2. **Nhãn phong cách / thẩm mỹ** mà thiết kế thật sự thể hiện.
   - Ví dụ: gingham + khung tem cổ điển → grandmacore, vintage; nơ, ren, hồng → coquette; sách, nến, gam tối → dark academia.
   - Chỉ gán nhãn khi có **ít nhất 2 dấu hiệu nhìn thấy**. Nhãn khớp yếu thì dùng ở bộ tag long-tail, không đưa vào tiêu đề.
3. **Cách khách đặt hàng**, suy ra từ thiết kế.
   - Ví dụ: chân dung thú cưng kèm tên → khách gửi ảnh và tên → "custom photo", "personalized".
   - Đây là suy luận. Phải nêu rõ là giả định trong Ghi chú.
4. **Từ đồng nghĩa của danh từ sản phẩm** mà người mua có thể gõ.
   - Ví dụ: sweatshirt / sweater / crewneck / pullover; mug / cup.
   - Chỉ dùng từ đồng nghĩa ở **tag**. Tiêu đề vẫn chỉ có 1 danh từ sản phẩm. Không gọi sai loại sản phẩm (sweatshirt không phải "tee").

## 2. Xác định mùa vụ từ thiết kế

Dựa vào các thành phần **nhìn thấy được** trên thiết kế để xếp sản phẩm vào 1 trong 3 loại:

| Loại | Dấu hiệu | Cách xử lý |
|---|---|---|
| **A. Làm riêng cho một dịp** | Bí ngô, bia mộ, ma cà rồng → Halloween; ông già Noel, cây thông → Christmas; trái tim kèm chữ Valentine… | Đưa **tên dịp vào tiêu đề** (đúng ngoại lệ của Etsy: dịp lễ là bản chất sản phẩm). Điền attribute Holiday/Occasion. Thêm tag theo dịp |
| **B. Theo mùa** | Lá phong, bông tuyết, hoa xuân, biển… nhưng không gắn với ngày lễ cụ thể | Được ghi mùa vào tiêu đề như một mô tả khách quan, ví dụ "Fall Leaves". Thêm tag theo mùa |
| **C. Dùng quanh năm** | Không có dấu hiệu mùa vụ | **Không** ghi dịp hay mùa vào tiêu đề. Dịp sắp tới chỉ đưa vào **tag** (người nhận, dịp mua) và đổi tag theo mùa |

**Thời điểm:**
- So ngày hiện tại với ngày diễn ra dịp hoặc mùa.
- Nếu có YTrends, gọi `ytrends_trend_calendar` (truyền tên dịp vào `keyword_or_tags`) để lấy ngày cao điểm, ngày nên bắt đầu đăng, và từ khóa theo mùa.
- **Cảnh báo** khi còn dưới khoảng 30 ngày tới dịp, hoặc khi đã qua ngày nên bắt đầu đăng. Listing mới cần thời gian để Etsy thu thập dữ liệu.
- Với loại A và B: gợi ý bộ tag thay thế cho giai đoạn **sau dịp** nếu thiết kế vẫn phù hợp (ví dụ sau Halloween vẫn còn mùa thu). Không đổi sang dịp mà thiết kế không thể hiện.

## 3. Nghiên cứu từ khóa

### Bước 3a – Lọc theo Etsy (bắt buộc)
Liệt kê từ khóa ứng viên theo 7 nhóm Etsy gợi ý:
1. Mô tả sản phẩm
2. Chất liệu / kỹ thuật
3. Phong cách
4. Người nhận
5. Dịp mua
6. Nhu cầu
7. Kích thước / hình dáng

Với nhóm 2 và 3, lấy từ phần "Soi ảnh" ở mục 1:
- **Nhóm 2:** mỗi kỹ thuật nhìn thấy phải có ít nhất 1 ứng viên, ví dụ "applique sweatshirt".
- **Nhóm 3:** có ít nhất 2 ứng viên phong cách, ví dụ "grandmacore clothing", "vintage crewneck". Nếu thiết kế không có phong cách rõ ràng, ghi lý do vào Ghi chú.

Loại ngay các từ khóa:
- **Sai trọng tâm.** Ví dụ: rồng chỉ là họa tiết nhỏ thì không lấy "dragon" làm từ khóa chính.
- **Có bản quyền hoặc thương hiệu:** tên sách, phim, nhân vật, tác giả, lời bài hát, trích dẫn tác phẩm, tên brand. Ví dụ: Fourth Wing, ACOTAR, Xaden, Disney.
  ⚠️ Công cụ dữ liệu thường đánh giá cao các tag này vì listing vi phạm bán chạy. **Không bao giờ dùng** nếu sản phẩm không có bản quyền.
- **Màu phôi**, trừ khi người dùng xác nhận sản phẩm chỉ có một màu.

### Bước 3b – Chấm điểm bằng YTrends (nếu có công cụ YTrends)
Với mỗi từ khóa ứng viên đã qua bước 3a, gọi `ytrends_research_keyword` (dạng concise, `ltype` phù hợp). Nếu gặp lỗi mạng (`retryable: true`), thử lại một lần. So sánh các chỉ số:

| Chỉ số | Cách đọc |
|---|---|
| `total_listings` / `total_sellers` | Mức cạnh tranh. Dưới khoảng 10 listing là chưa đủ dữ liệu, đừng kết luận |
| `avg_conversion_rate` | Chuyển đổi trung bình. So giữa các từ khóa với nhau |
| `opportunity_score` | Điểm cơ hội tổng hợp. Càng cao càng dễ cạnh tranh |
| `measured_demand.pct_sold_in_window` | % listing có ước tính bán ra. So với mức chung toàn sàn mà công cụ báo (~32%) |

- Gọi `response_format: "detailed"` **một lần** cho từ khóa lõi để lấy `related_keywords`. Các từ khóa liên quan này phải lọc lại qua bước 3a.
- Từ khóa chưa đủ dữ liệu nhưng **mô tả chính xác** sản phẩm vẫn được dùng. Ghi chú là "chưa có số liệu".
- **Ghi lại số liệu của mọi từ khóa xuất hiện trong output** (mọi tiêu đề, mọi bộ tag) để đưa vào bảng số liệu ở mục 10. Nghĩa là mọi tag trong mọi bộ đều phải được tra, không chỉ cụm lõi.
- Ghi lại `snapshot.as_of_date`, `snapshot.median_data_age_days` và trường `link` của từng từ khóa để dẫn nguồn.
- **Chép số đúng từ kết quả công cụ.** Chỉ được làm tròn (phần trăm 1 chữ số thập phân, điểm 1 chữ số thập phân). Không ước lượng, không suy ra số cho từ khóa chưa tra.
- **Giới hạn của dữ liệu:**
  - YTrends chỉ index một phần của Etsy và dữ liệu thường đã cũ vài tuần đến vài tháng.
  - Số "bán ra" là ước tính.
  - → Chỉ dùng để **xếp hạng tương đối** các từ khóa, không trích dẫn như số tuyệt đối.

Không có YTrends: chọn theo nguyên tắc long-tail của Etsy (cụm cụ thể, 2–3 từ). Sau khi đăng, kiểm chứng bằng Shop Stats.

### Bước 3c – Chọn
- **1–3 cụm lõi:** đúng sản phẩm nhất và có dữ liệu tốt nhất. Những cụm này sẽ có ở **cả tiêu đề và tag**.
- **~10 cụm phụ:** đa dạng, nhắm vào truy vấn mà tiêu đề chưa có.

### Bước 3d – Phân tích listing đối thủ (khi người dùng đưa)
Mục đích: **lấy từ khóa tốt của đối thủ, không chép cách viết của họ.**

1. **Tách từ khóa.** Tách tiêu đề đối thủ thành các cụm. Coi mỗi tag và mỗi cụm là một ứng viên.
2. **Lọc qua bước 3a.** Loại cụm vi phạm (bản quyền, sai trọng tâm, thành phần không có trong thiết kế của người dùng…). Ghi rõ lý do.
3. **Tra YTrends** mọi cụm còn lại, như bước 3b.
4. **Phân loại từng cụm:**

   | Nhãn | Khi nào |
   |---|---|
   | **Lấy** | Đúng sản phẩm, có số liệu tốt (hoặc là từ mô tả chính xác), và bản hiện tại chưa có |
   | **Đã có** | Trùng hoặc gần trùng với từ khóa đã chọn |
   | **Bỏ** | Vi phạm rule, quá rộng (ví dụ "unique birthday gift"), mơ hồ (ví dụ "stamp design"), tag bị cắt hoặc sai chính tả (ví dụ "Personalized Pet Gif"), hoặc gọi sai loại sản phẩm |

5. **Chỉ ra lỗi rule trong cách viết của đối thủ.** Đếm bằng công cụ: số ký tự, số từ, số lần danh từ sản phẩm xuất hiện, cụm quà tặng trong tiêu đề, từ lặp.
6. **Không kết luận "đối thủ bán tốt nhờ tiêu đề".** Thứ hạng phụ thuộc chuyển đổi, ảnh, review, giá, lịch sử bán và tuổi listing. Vị trí từ trong tiêu đề không ảnh hưởng thứ hạng (xem mục 0).
7. **Đưa các cụm "Lấy" vào phương án.** Cập nhật tiêu đề và bộ tag. Cụm "Lấy" phải thay cho tag yếu nhất (số liệu thấp nhất hoặc chưa có số liệu), không được làm bộ tag vượt 13.

## 4. TITLE

### Giới hạn
- **Cứng (luật Etsy):** ≤ 140 ký tự.
- **Mục tiêu (hướng dẫn Etsy):** < 15 từ, thường rơi vào khoảng 60–110 ký tự.
- Dùng đủ 140 ký tự không phạm luật, nhưng đi ngược hướng dẫn. Etsy đã sửa thuật toán chính vì tiêu đề dài, nhồi từ khóa.
- URL của listing được tạo từ tiêu đề **lúc publish lần đầu** và không đổi sau đó.

### Bảng giữ hay bỏ (dựa trên bảng chính thức của Etsy)

| Loại từ | Ví dụ | Giữ? |
|---|---|---|
| Danh từ sản phẩm | sweatshirt, mug, ring | **Có, đúng 1 lần** |
| Mô tả khách quan | chất liệu, kích thước, kỹ thuật, vintage | **Có**. Chất liệu và size chỉ khi người dùng cung cấp. Màu phôi: xem nguyên tắc 4 |
| Dịp lễ, mùa | Halloween, Christmas, Fall | Theo bảng mùa vụ ở mục 2 |
| Người nhận | gift for her, teacher gift | **Không**, đưa vào tag |
| Từ cảm tính | perfect, beautiful, cute | **Không**, đưa vào description |
| Thông tin bán hàng | sale, free shipping, % off | **Không**, xóa hẳn |
| Từ hoặc cụm lặp | unisex adult poncho, unisex cotton poncho | **Không** |

### Thứ tự từ: đặt câu chữ lên đầu hay loại sản phẩm lên đầu?
Thứ tự không ảnh hưởng thứ hạng, chỉ ảnh hưởng người mua (vài từ đầu trên Etsy) và Google (**50–60 ký tự đầu**).

**Đặt câu chữ / tên thiết kế lên đầu** khi thỏa **cả 4** điều kiện:
1. Câu chữ là thành phần chính của thiết kế.
2. Câu ngắn, sao cho danh từ sản phẩm vẫn nằm trong 60 ký tự đầu (thực tế khoảng ≤ 5 từ).
3. Câu chữ không có bản quyền.
4. Có người tìm theo câu đó (YTrends có listing hoặc tag dùng câu này, hoặc đây là câu quen thuộc trong ngách).

**Ngược lại, đặt loại sản phẩm lên đầu.** Ví dụ: thiết kế chủ yếu là hình, câu dài, hoặc câu chung chung.

**Luôn bắt buộc:**
- Danh từ sản phẩm nằm trong 60 ký tự đầu.
- Tiêu đề chứa **nguyên cụm** ít nhất 1 từ khóa lõi (ví dụ "bookish sweatshirt", "halloween sweatshirt").

### Ví dụ chính thức của Etsy (trước → sau)
- Dad T-Shirt | Father Shirt | Personalized Father's Day Gift | … → **Personalized 100% Cotton Dad T-Shirt: Custom Kids' Names S-XL**
- Moonstone Ring Mini Ring Solid Gold Perfect For Women's Wedding … → **Celestial Blue Moonstone Ring, 9k Solid Gold Band**
- ON SALE ! Birthday Bandana - Happy Birthday, Birthday Dog Bandana … → **Birthday Bones Cotton Dog Bandana - Easy Slip Over the Collar**

## 5. TAGS

### Giới hạn cứng (Help Center)
- **13 tag**, luôn dùng đủ.
- Mỗi tag **≤ 20 ký tự** (tính cả dấu cách).
- Chỉ dùng chữ, số, dấu cách. Được dùng `'` và `-` bên trong từ, nhưng không đặt ở đầu tag.

### Rule
1. **Tag phải đúng với sản phẩm** (bắt buộc). Tag không cần liên quan tới tiêu đề.
2. **Trùng giữa tiêu đề và tag:**
   - Việc từ khóa phải có ở cả hai nơi mới được match là **hiểu lầm**. Etsy đã xác nhận trong podcast Mythbusting.
   - Nhưng Etsy khuyên đặt **từ khóa mạnh nhất** ở cả hai nơi, vì có thể tăng độ liên quan.
   - → Chỉ 1–3 cụm lõi được trùng. Các tag còn lại nhắm vào truy vấn mới.
3. **Cụm 2–3 từ, long-tail.** Ví dụ: "custom bracelet" tốt hơn 2 tag "custom" và "bracelet". Mẹo nhanh: nếu không tưởng tượng được ai gõ cụm này vào Google thì đừng dùng.
4. **Không lặp hoặc gần lặp giữa các tag.** Ví dụ: "octopus art print" + "animal wall decor" tốt hơn "octopus art" + "octopus print".
5. **Không trùng nguyên văn category hoặc attribute đã chọn.** Ví dụ: attribute Holiday là Halloween thì không cần tag "halloween" đứng riêng. Vẫn được ghép vào cụm dài hơn, ví dụ "halloween crewneck".
6. **Không thêm biến thể số ít/số nhiều, không cố tình viết sai chính tả, không trộn ngôn ngữ.**
7. **Dùng từ đồng nghĩa và cách gọi theo vùng** khi có người mua dùng. Ví dụ: thong sandals / flip flops; sweatshirt / sweater / crewneck (lấy từ phần "Soi ảnh" ở mục 1).
8. **Cụm quà tặng, dịp mua, người nhận** để ở tag, không để ở tiêu đề.
9. **Cụm dài hơn 20 ký tự:** tách thành nhiều cụm nhỏ. Nếu là cụm lõi, để nguyên cụm đó ở tiêu đề.
10. **Bao phủ ít nhất 5 trong 7 nhóm** ở bước 3a.

## 6. CATEGORY & ATTRIBUTE

- Chọn **subcategory cụ thể nhất**. Listing tự xuất hiện trong mọi category cha.
- Điền **tất cả attribute đúng với sản phẩm**, kể cả khi kém chính xác hơn cách mình mô tả. Ví dụ: len màu "magenta" vẫn chọn màu Pink.
- Attribute dịp lễ chỉ dùng cho sản phẩm **làm riêng cho dịp đó** (loại A ở mục 2). Sản phẩm chỉ "phù hợp" với dịp đó thì dùng tag.
- **Attribute màu:** skill không tự chọn màu phôi. Người dùng tự chọn khi đăng listing, theo màu và variation thực tế mà shop bán.

## 7. DESCRIPTION

- **Câu đầu tiên** nói rõ đây là sản phẩm gì và chứa 2–3 từ khóa lõi một cách tự nhiên. Người đọc câu đầu phải biết ngay mình đang xem gì.
- **Không chép lại nguyên tiêu đề**, không liệt kê từ khóa, không lặp một cụm nhiều lần.
- **Mô tả thiết kế** dựa trên những gì nhìn thấy được: thành phần, vị trí, màu của thiết kế. Không ghi màu phôi (nguyên tắc 4).
- **Các mục thông tin chỉ xuất hiện khi người dùng có cung cấp dữ liệu.** Mục nào không có dữ liệu thì bỏ cả mục, không để tiêu đề mục rỗng:
  - Details (chất liệu, size, form)
  - How to order
  - Care
  - Processing & shipping
- Dùng bullet hoặc đoạn ngắn.
- Kết thúc bằng một đoạn kể chuyện hoặc gợi ý quà tặng. Từ cảm tính và cụm quà tặng được phép dùng ở đây.

## 8. Đưa ra nhiều phương án

Mỗi phần phải có **2–3 phương án khác nhau thật sự về chiến lược**, không chỉ đảo vài từ. Nếu không có đủ chiến lược hợp lệ, đưa 2 phương án và nói rõ vì sao bỏ phương án thứ 3.

| Phần | Các chiến lược gợi ý |
|---|---|
| **Title** (2–3) | ① Loại sản phẩm lên đầu ② Câu chữ / tên thiết kế lên đầu (chỉ khi đạt 4 điều kiện ở mục 4) ③ Mùa vụ lên đầu (chỉ với loại A/B ở mục 2), hoặc một góc từ khóa lõi khác |
| **Tags** (2–3 bộ, mỗi bộ đủ 13) | ① Cân bằng (phủ đủ các nhóm) ② Mùa vụ (với loại A/B), hoặc bộ dùng sau dịp ③ Long-tail, ít cạnh tranh |
| **Description** (2–3) | ① Kể chuyện ② Ngắn gọn dạng bullet ③ Quà tặng / mùa vụ |

**Với mỗi phương án:**
- Ghi **1–3 gạch đầu dòng lý do**: rule Etsy nào áp dụng, số liệu YTrends nào (nếu có). Lý do phải **dẫn số cụ thể**, ví dụ "halloween sweatshirt: 2.542 listing, 48,0% có ước tính bán ra", không viết chung chung kiểu "từ khóa mạnh".
- Với mỗi bộ tag, ghi thêm một dòng tóm tắt: số tag có số liệu / 13, và số tag có tỷ lệ "có bán" cao hơn mức chung toàn sàn.
- Đánh dấu **⭐ Đề xuất** cho đúng 1 phương án của mỗi phần.
- Bộ tag phải ăn khớp với tiêu đề tương ứng: cụm lõi của bộ tag phải có trong tiêu đề.
- **Mỗi phương án đều phải đạt checklist ở mục 9.**

**Nút copy:**
- Mỗi phương án (một tiêu đề, một bộ tag, một mô tả) nằm trong **một khối code riêng** dạng ` ```text `, để ứng dụng Claude hiển thị nút Copy.
- Bộ tag viết trên **một dòng**, ngăn cách bằng dấu phẩy.
- **Không** đặt chú thích, số ký tự hay lý do bên trong khối code. Những thông tin đó để ngay phía trên khối code.

## 9. Checklist (bắt buộc chạy cho từng phương án trước khi trả kết quả)

**Title**
- [ ] ≤ 140 ký tự, < 15 từ (đếm bằng công cụ, không ước lượng)
- [ ] Danh từ sản phẩm xuất hiện đúng 1 lần và nằm trong 60 ký tự đầu
- [ ] Chứa nguyên cụm ít nhất 1 từ khóa lõi
- [ ] Không có từ cảm tính, cụm quà tặng, thông tin bán hàng, từ lặp
- [ ] Không có màu phôi (trừ khi người dùng xác nhận chỉ bán 1 màu)
- [ ] Dịp lễ hoặc mùa chỉ có mặt khi thiết kế thuộc loại A hoặc B
- [ ] Không có bản quyền hoặc thương hiệu; mô tả đúng trọng tâm sản phẩm
- [ ] Không có thông tin người dùng chưa cung cấp

**Tag**
- [ ] Đúng 13 tag, mỗi tag ≤ 20 ký tự (đếm bằng công cụ, không ước lượng)
- [ ] Chỉ chữ, số, dấu cách, `'`, `-`; không bắt đầu bằng `'` hoặc `-`
- [ ] Không lặp hoặc gần lặp; không trùng category hoặc attribute
- [ ] 1–3 cụm lõi trùng với tiêu đề, các tag còn lại nhắm truy vấn mới
- [ ] Không có bản quyền, thương hiệu hay màu phôi; mọi tag đúng với sản phẩm
- [ ] Bao phủ ≥ 5/7 nhóm
- [ ] Mọi kỹ thuật nhìn thấy (kể cả kỹ thuật phụ) có mặt ở tiêu đề hoặc ít nhất 1 bộ tag
- [ ] Có ít nhất 1 tag phong cách trong ít nhất 1 bộ (hoặc Ghi chú đã nêu lý do không có)
- [ ] Nếu có listing đối thủ: mọi cụm "Lấy" ở bước 3d đã có mặt trong ít nhất 1 phương án

**Số liệu**
- [ ] Mọi từ khóa trong mọi tiêu đề và bộ tag đều có dòng trong bảng số liệu (có số, "chưa đủ dữ liệu" hoặc "chưa tra được")
- [ ] Mọi con số khớp với kết quả công cụ; không có số ước lượng hay số tự suy ra
- [ ] Có ghi nguồn, ngày dữ liệu và câu lưu ý về giới hạn dữ liệu
- [ ] Lý do của từng phương án dẫn số cụ thể

**Description**
- [ ] Câu đầu nói rõ sản phẩm và chứa từ khóa lõi
- [ ] Không có màu phôi, không có chỗ trống `[ ]`, không có thông tin bịa
- [ ] Không có mục rỗng

## 10. Định dạng output

````
## Phân tích nhanh
- Sản phẩm / thành phần chính / câu chữ
- Soi ảnh: kỹ thuật (chính + phụ) / phong cách / cách khách đặt hàng / từ đồng nghĩa
- Mùa vụ: loại A, B hoặc C + cảnh báo thời điểm (nếu có)
- Từ khóa lõi đã chọn + số liệu (nếu có YTrends)

## TITLE
### Phương án 1 ⭐ Đề xuất – <tên chiến lược> (<số ký tự> ký tự, <số từ> từ)
- Lý do...
```text
<title>
```
### Phương án 2 – ...
### Phương án 3 – ...

## TAGS
### Bộ 1 ⭐ Đề xuất – <tên chiến lược>
- Lý do...
```text
tag1, tag2, ..., tag13
```
### Bộ 2 – ...
### Bộ 3 – ...

## BẢNG SỐ LIỆU TỪ KHÓA
Nguồn: YTrends · Ngày dữ liệu: <as_of_date> · Tuổi dữ liệu trung vị: <median_data_age_days> ngày · Mức "có bán" chung toàn sàn: ~<x>%

| Từ khóa | Dùng ở | Listing | Shop | Chuyển đổi | Opp score | % có bán (ước tính) | Cạnh tranh | Nhận định |
|---|---|---|---|---|---|---|---|---|
| <từ khóa> | Title P1, Bộ 1, Bộ 2 | 2.542 | 1.154 | 2,1% | 26,9 | 48,0% | high | Nhu cầu cao, cạnh tranh cao |
| <từ khóa> | Bộ 3 | 5 | 5 | 2,7% | – | – | low | Chưa đủ dữ liệu (< 10 listing) |
| <từ khóa> | Bộ 1 | – | – | – | – | – | – | Chưa tra được (lỗi công cụ) |

- Sắp xếp: cụm lõi trước, sau đó theo % có bán giảm dần.
- Dưới bảng ghi: *"Số liệu là ảnh chụp một phần dữ liệu Etsy do YTrends index, số bán là ước tính (chuyển đổi × lượt xem). Dùng để so sánh tương đối giữa các từ khóa, không phải doanh số thực."*
- Kèm link YTrends của 1–3 cụm lõi để người dùng tự kiểm chứng.
- **Không có YTrends:** vẫn giữ mục này nhưng ghi "Không có dữ liệu YTrends trong phiên này". Bảng chỉ còn cột Từ khóa, Dùng ở, Số ký tự. Không tự bịa số liệu.

## SO SÁNH VỚI LISTING ĐỐI THỦ (chỉ khi người dùng đưa listing đối thủ)
- Lỗi rule trong tiêu đề và tag của đối thủ (có số đếm bằng công cụ)
- Bảng từng cụm của đối thủ: Cụm | Số ký tự | Lấy / Đã có / Bỏ | Lý do | Số liệu YTrends
- Một câu: kết quả bán hàng của đối thủ không chứng minh cách viết tiêu đề của họ hiệu quả

## CATEGORY & ATTRIBUTES
<subcategory cụ thể nhất; các attribute nên điền, trừ màu phôi>

## DESCRIPTION
### Phiên bản 1 ⭐ Đề xuất – <phong cách>
```text
<description>
```
### Phiên bản 2 – ...
### Phiên bản 3 – ...

## GHI CHÚ
- Từ khóa đã loại và lý do (sai trọng tâm / bản quyền / dữ liệu kém / màu phôi)
- Thông tin tùy chọn nào nếu bổ sung sẽ làm listing tốt hơn (1 dòng)
````

## 11. Ví dụ mẫu (rút gọn)

**Sản phẩm:** sweatshirt thêu chữ "just one more chapter", thanh kiếm, cuốn sách mở, 2 tiên, 2 rồng nhỏ. Tay trái thêu hoa hồng đỏ, tay phải thêu trăng lưỡi liềm và pha lê tím. Người dùng không cung cấp chất liệu, size hay màu phôi.

**Mùa vụ:** loại C, dùng quanh năm. Vì vậy chỉ có 2 phương án tiêu đề: không có chiến lược mùa vụ hợp lệ.

**Title – Phương án 1 ⭐ Đề xuất: câu chữ lên đầu** (75 ký tự, 11 từ)
- Câu chữ ngắn, là thành phần chính, đạt cả 4 điều kiện.
- Chứa nguyên cụm lõi "bookish sweatshirt".
```text
Just One More Chapter Embroidered Bookish Sweatshirt, Rose and Moon Sleeves
```

**Title – Phương án 2: loại sản phẩm lên đầu** (84 ký tự, 12 từ)
- Có thêm "fantasy", ứng với cụm có opp score cao trên YTrends.
```text
Embroidered Fantasy Bookish Sweatshirt: Just One More Chapter, Rose and Moon Sleeves
```

**Tags – Bộ 1 ⭐ Đề xuất: cân bằng**
- Trùng với tiêu đề: "bookish sweatshirt" và "one more chapter".
- Đã loại các tag Fourth Wing / Xaden / ACOTAR vì có bản quyền.
```text
bookish sweatshirt, fantasy sweatshirt, dragon sweatshirt, dragon book shirt, bookworm sweatshirt, bookish crewneck, sleeve embroidery, romantasy reader, fantasy reader gift, book lover gift, dark academia, book club gift, one more chapter
```

**Description – Phiên bản 1 ⭐ Đề xuất: kể chuyện**
```text
"Just one more chapter" – the promise every fantasy reader makes at 2 a.m. This embroidered bookish sweatshirt stitches that feeling onto a cozy crewneck, with a gold-hilted sword, an open book, dragons and fairies across the front.

Each sleeve tells its own story: a red rose vine with golden thorns on one side, and a crescent moon cradling a purple crystal on the other.

✦ MADE FOR READERS
For the romantasy reader, the book club friend, or the bookworm who never stops at one chapter – a gift any book lover will reach for all season.
```

## Nguồn (tài liệu chính thức của Etsy)

- New Guidance for Listing Titles, and a Tool to Help (27/04/2026): https://www.etsy.com/seller-handbook/article/1399426136697
- Keywords 101: Everything You Need to Know (08/2025): https://www.etsy.com/seller-handbook/article/382774281517
- How Etsy Search Works (08/2025): https://www.etsy.com/seller-handbook/article/375461474487
- The Anatomy of a Well-Crafted Etsy Listing (08/2025): https://www.etsy.com/seller-handbook/article/1347574487014
- Podcast Transcript: Etsy Search Mythbusting With Two Etsy Experts: https://www.etsy.com/seller-handbook/article/397558006917
- Podcast Transcript: Insider's Guide to Etsy Search, Keywords Edition (25/08/2021): https://www.etsy.com/seller-handbook/article/1046872470801
- Help Center – How to Use Tags to Get Found in Search: https://help.etsy.com/hc/en-us/articles/360000336307
- Help Center – How to Create a Listing: https://help.etsy.com/hc/en-us/articles/115015628707
- Help Center – Search Engine Optimization (SEO) for Shop and Listing Pages: https://help.etsy.com/hc/en-us/articles/115015663987
