# 🧮 Factorial Calculator App

Một ứng dụng web tính giai thừa được xây dựng bằng **Streamlit** với hệ thống đăng nhập và quản lý người dùng.

## 📋 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng chính](#-tính-năng-chính)
- [Cài đặt](#-cài-đặt)
- [Cách sử dụng](#-cách-sử-dụng)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [API Reference](#-api-reference)
- [Screenshots](#-screenshots)
- [Đóng góp](#-đóng-góp)
- [Giấy phép](#-giấy-phép)

## 🎯 Giới thiệu

**Factorial Calculator App** là một ứng dụng web đơn giản nhưng mạnh mẽ cho phép người dùng:
- Đăng nhập với hệ thống xác thực
- Tính giai thừa của các số từ 0 đến 900
- Quản lý danh sách người dùng qua file upload
- Giao diện thân thiện và dễ sử dụng

## ✨ Tính năng chính

### 🔐 Hệ thống đăng nhập
- **Xác thực người dùng** dựa trên danh sách có sẵn
- **Quản lý session** để duy trì trạng thái đăng nhập
- **Trang chào hỏi** cho người dùng không có quyền truy cập

### 📁 Quản lý người dùng
- **Hiển thị danh sách** người dùng hiện tại
- **Upload file txt** để cập nhật danh sách người dùng
- **Preview nội dung** file trước khi cập nhật
- **Tự động merge** và loại bỏ trùng lặp

### 🧮 Tính giai thừa
- **Tính toán nhanh** với thuật toán tối ưu
- **Hỗ trợ số lớn** (lên đến 900!)
- **Xử lý lỗi** cho các trường hợp đặc biệt
- **Giao diện đẹp** với animation loading

### 🎨 Giao diện người dùng
- **Responsive design** hoạt động trên mọi thiết bị
- **Icons và animations** tăng trải nghiệm người dùng
- **Thông báo rõ ràng** cho mọi hành động
- **Phân chia logic** giữa các trang

## 🚀 Cài đặt

### Yêu cầu hệ thống
- Python 3.7+
- pip (Python package manager)

### Cài đặt nhanh

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/factorial-app.git
   cd factorial-app
   ```

2. **Cài đặt dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy ứng dụng**
   ```bash
   streamlit run app.py
   ```

4. **Mở trình duyệt** tại `http://localhost:8501`

### Cài đặt trong môi trường ảo (khuyến nghị)

```bash
# Tạo môi trường ảo
python -m venv factorial_env

# Kích hoạt môi trường ảo
# Windows
factorial_env\Scripts\activate
# Linux/Mac
source factorial_env/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run app.py
```

## 🔧 Cách sử dụng

### Đăng nhập lần đầu

1. **Khởi động ứng dụng** theo hướng dẫn cài đặt
2. **Sử dụng tài khoản mặc định**:
   - `admin`
   - `aivietnam`
   - `quocthai`
   - `quangvinh`

### Thêm người dùng mới

1. **Tạo file txt** chứa danh sách tên người dùng:
   ```
   nguyenvan
   tranhoang
   lethimai
   ```

2. **Upload file** qua giao diện web
3. **Xem preview** và xác nhận cập nhật
4. **Đăng nhập** bằng tên người dùng mới

### Tính giai thừa

1. **Đăng nhập** thành công
2. **Nhập số** từ 0 đến 900
3. **Nhấn "Tính giai thừa"** để xem kết quả
4. **Đăng xuất** khi hoàn thành

## 📁 Cấu trúc dự án

```
factorial-app/
├── app.py                 # Ứng dụng chính Streamlit
├── factorial.py           # Module tính giai thừa
├── requirements.txt       # Dependencies
├── user.txt              # Danh sách người dùng
├── README.md             # Tài liệu này
└── aio_project_1_1.ipynb # Notebook phát triển gốc
```

### Mô tả files

| File | Mô tả |
|------|-------|
| `app.py` | Ứng dụng web chính với giao diện Streamlit |
| `factorial.py` | Module chứa hàm tính giai thừa |
| `requirements.txt` | Danh sách thư viện Python cần thiết |
| `user.txt` | File chứa danh sách người dùng được phép truy cập |
| `README.md` | Tài liệu hướng dẫn sử dụng |

## 📚 API Reference

### Hàm chính trong `factorial.py`

```python
def fact(n):
    """
    Tính giai thừa của một số nguyên không âm.
    
    Args:
        n (int): Số nguyên không âm cần tính giai thừa
        
    Returns:
        int: Giai thừa của n
        str: "Không xác định" nếu n < 0
    """
```

### Hàm chính trong `app.py`

```python
def load_users():
    """Đọc danh sách user từ file user.txt"""

def save_users(users_list):
    """Lưu danh sách users vào file user.txt"""

def process_uploaded_file(uploaded_file):
    """Xử lý file txt được upload và trích xuất danh sách users"""
```

## 📸 Screenshots

### Trang đăng nhập
- Hiển thị danh sách người dùng hiện tại
- Form upload file người dùng mới
- Form đăng nhập

### Trang tính giai thừa
- Chào mừng người dùng
- Input số cần tính giai thừa
- Hiển thị kết quả với animation

### Trang chào hỏi
- Thông báo cho người dùng không có quyền
- Nút quay lại đăng nhập

## 🛠️ Khắc phục sự cố

### Lỗi thường gặp

1. **File user.txt không tồn tại**
   ```
   Giải pháp: Tạo file user.txt với danh sách người dùng
   ```

2. **Streamlit không khởi động**
   ```
   Giải pháp: Kiểm tra Python version và cài đặt lại dependencies
   ```

3. **Không thể upload file**
   ```
   Giải pháp: Kiểm tra định dạng file (chỉ chấp nhận .txt)
   ```

### Debug mode

Chạy ứng dụng với debug mode:
```bash
streamlit run app.py --logger.level=debug
```

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Để contribute:

1. **Fork** repository
2. **Tạo branch** mới (`git checkout -b feature/amazing-feature`)
3. **Commit** thay đổi (`git commit -m 'Add some amazing feature'`)
4. **Push** lên branch (`git push origin feature/amazing-feature`)
5. **Tạo Pull Request**

### Quy tắc đóng góp

- Viết code rõ ràng và có comment
- Tuân thủ PEP 8 style guide
- Thêm tests cho tính năng mới
- Cập nhật documentation

## 📝 Changelog

### Version 1.0.0 (2024-01-XX)
- ✅ Hệ thống đăng nhập cơ bản
- ✅ Tính giai thừa với giao diện web
- ✅ Quản lý người dùng qua file txt
- ✅ Upload file để cập nhật danh sách người dùng
- ✅ Giao diện responsive và thân thiện

## 🔒 Bảo mật

- Dữ liệu người dùng được lưu trữ cục bộ
- Không thu thập thông tin cá nhân
- Session được quản lý an toàn qua Streamlit

## 📞 Liên hệ

- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Project Link**: [https://github.com/yourusername/factorial-app](https://github.com/yourusername/factorial-app)

## 📄 Giấy phép

Dự án này được cấp phép theo [MIT License](LICENSE) - xem file LICENSE để biết chi tiết.

---

<div align="center">
  <p><strong>Được phát triển với ❤️ bởi [Tên của bạn]</strong></p>
  <p>⭐ Nếu project này hữu ích, hãy star repository!</p>
</div>
