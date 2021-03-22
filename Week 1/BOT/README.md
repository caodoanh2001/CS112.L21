# BOT - TRẠM THU PHÍ

## 1. Abstraction(Trừu tượng hóa):
- Tìm p,q  (1 <= p <= q <= n) và mảng con lớn nhất nằm trong khoảng p đến q. Nếu có nhiều cách chọn thì chọn p nhỏ nhất
## 2. Pattern recognition(Nhận dạng mẫu):
- Kỹ thuật áp dụng: Duyệt
- Đặc điểm nhận dạng: Chọn khoảng từ `p` đến `q` sao cho `lợi nhuận` *cao nhất* hoặc *lỗ ít nhất*
## 3. Algorithm designed(Thiết kế thuật toán):
- Nếu `a[i] < 0` với mọi `i = 1 -> n`:
  -  Tổng lãi = `max{a[i], i = 1 -> n}`
  -  Khoảng cần tìm chỉ chứa `1 phần tử`
- Nếu `a[i] = 0` với mọi `i = 1 -> n`:
  -  Tổng lãi = `0`
  -  Khoảng cần tìm chỉ chứa `1 phần tử`
- Nếu ***tồn tại*** `a[i] > 0`:
  -  Tính tổng `sum` các phần tử liên tiếp từ `p` đến `q` (p bắt đầu từ 1):
		-  Nếu `sum > 0`:
		    - Lưu giá trị `tổng lớn nhất`
		    - Lưu vị trí khoảng cần tìm
		-  Nếu `sum = 0`:
		    - `Bỏ qua` vị trí khoảng đã duyệt
		    - Gán lại giá trị cho `sum = 0`

## 4. Complexity(Độ phức tạp):
- Ta chỉ chạy một vòng lặp cho chương trình nên độ phức tạp là `O(n)`
