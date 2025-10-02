# 📝 Test Cases - Form Đăng Nhập

Dưới đây là 6 test case tối thiểu theo yêu cầu đề bài.

---

## ✅ Danh sách Test Case

| **STT** | **Tên Test Case**            | **Bước thực hiện**                                                                 | **Kết quả mong đợi**                                        |
|---------|-------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------|
| 1       | Đăng nhập thành công          | - Nhập `username` hợp lệ <br> - Nhập `password` hợp lệ <br> - Click **LOGIN**       | Hệ thống chuyển sang trang **Dashboard** hoặc báo *"Login success!"* |
| 2       | Sai thông tin đăng nhập       | - Nhập `username` đúng <br> - Nhập `password` sai <br> - Click **LOGIN**            | Hiển thị thông báo lỗi (*"Invalid credentials."*)      |
| 3       | Bỏ trống trường               | - Để trống **Username** hoặc **Password** <br> - Click **LOGIN**                    | Hiển thị cảnh báo yêu cầu nhập đầy đủ thông tin              |
| 4       | Link "Forgot password?"       | - Click vào link **Forgot password?**                                               | Điều hướng sang trang **Quên mật khẩu**                     |
| 5       | Link "SIGN UP"                | - Click vào link **SIGN UP**                                                        | Điều hướng sang trang **Đăng ký**                           |
| 6       | Nút Social Login              | - Kiểm tra hiển thị đủ 3 nút **Facebook, Twitter, Google** <br> - Click từng nút     | Mỗi nút đều **click được** và hiển thị alert |

---

 
