# SEAWEED - TẢO BIỂN

## 1. Abstraction(Trừu tượng hóa):
- Tính kết quả `n * Fibonacci(2k + 1)`

## 2. Pattern recognition(Nhận dạng mẫu):
- Kỹ thuật áp dụng: Đệ quy/Nhân ma trận
- Đặc điểm nhận dạng:

Với số cá thể `n = 1`, ta có bảng sinh sản dưới đây
   
| NGÀY \ MỨC |  1  |  2  |  3  |  4  |  5  |  6  |  Tổng  |
|:----------:|:---:|:---:|:---:|:---:|:---:|:---:|:------:|
|      0     |  1  |  -  |  -  |  -  |  -  |  -  |    1   |
|      1     |  1  |  1  |  -  |  -  |  -  |  -  |    3   |
|      2     |  3  |  1  |  1  |  -  |  -  |  -  |    5   |
|      3     |  8  |  3  |  1  |  1  |  -  |  -  |   13   |
|      4     | 21  |  8  |  3  |  1  |  1  |  -  |   34   |
|      5     | 55  | 21  |  8  |  3  |  1  |  1  |   89   |

Từ bảng trên, ta thấy có dạng giống với Fibonacci. Ta có bảng Fibonacci dưới đây:
  
|  GIÁ TRỊ \ k |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |  11  |
|:------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|:----:|
|    Fibo(k)   |  0  |  1  |  1  |  2  |  3  |  5  |  8  |  13 |  21 |  34 |  55  |  89  |
| Fibo(2k + 1) |  1  |  3  |  5  | 13  | 34  |  89 | 233 | 610 |     |     |      |      |

Từ hai bảng trên, ta suy ra được `kết quả` của `n` cá thể sau `k` ngày là: `n * Fibonacci(2k + 1)`
## 3. Algorithm designed(Thiết kế thuật toán):
### 3.1. Đệ quy
- Fibonacci dùng đệ quy thì ta có 3 trường hợp xảy ra:
  - Nếu `n = 0` trả về `0`
  - Nếu `n = 1` trả về `1`
  - Trường hợp còn lại trả về `Fibonacci(n - 1) + Fibonacci(n - 2)`
### 3.2. Nhân ma trận ([Fibonacci Q-Matrix](https://mathworld.wolfram.com/FibonacciQ-Matrix.html))
- Fibonacci dùng nhân ma trận:
  
## 4. Complexity(Độ phức tạp):
### 4.1. Đệ quy
- Đối với đệ quy thì ta không có quy chuẩn nào để đánh giá độ phức tạp, ở trường hợp này ta thấy số Fibonacci tăng theo cấp số nhân
- Độ phức tạp trong trường hợp này: `O(2^n)`
### 4.2. Nhân ma trận ([Fibonacci Q-Matrix](https://mathworld.wolfram.com/FibonacciQ-Matrix.html))

## 5. Jupyter notebook: [Click here](./SEAWEED.ipynb)
