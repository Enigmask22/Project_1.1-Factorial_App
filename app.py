import streamlit as st
from factorial import fact
import os

def load_users():
    """Đọc danh sách user từ file user.txt"""
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("File user.txt không tồn tại!")
            return []
    except Exception as e:
        st.error(f"Lỗi khi đọc file user.txt: {e}")
        return []

def save_users(users_list):
    """Lưu danh sách users vào file user.txt"""
    try:
        with open("user.txt", "w", encoding="utf-8") as f:
            for user in users_list:
                f.write(user + "\n")
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file user.txt: {e}")
        return False

def process_uploaded_file(uploaded_file):
    """Xử lý file txt được upload và trích xuất danh sách users"""
    try:
        # Đọc nội dung file được upload
        content = uploaded_file.read().decode("utf-8")
        new_users = [line.strip() for line in content.splitlines() if line.strip()]
        
        # Lấy danh sách users hiện tại
        current_users = load_users()
        
        # Merge danh sách (loại bỏ trùng lặp)
        all_users = list(set(current_users + new_users))
        all_users.sort()  # Sắp xếp theo thứ tự alphabetical
        
        return all_users
    except Exception as e:
        st.error(f"Lỗi khi xử lý file: {e}")
        return []

def login_page():
    """Trang đăng nhập"""
    st.title("Đăng nhập")
    
    # Hiển thị danh sách users hiện tại
    with st.expander("📋 Danh sách users hiện tại"):
        current_users = load_users()
        if current_users:
            st.write("**Các tài khoản được phép:**")
            for user in current_users:
                st.write(f"• {user}")
        else:
            st.write("Không có users nào trong hệ thống.")
    
    # Phần tải lên file mới
    st.markdown("---")
    st.subheader("📁 Cập nhật danh sách users")
    
    uploaded_file = st.file_uploader(
        "Tải lên file txt chứa danh sách users mới:",
        type=['txt'],
        help="File txt với mỗi user trên một dòng"
    )
    
    if uploaded_file is not None:
        # Hiển thị preview nội dung file
        with st.expander("👀 Xem trước nội dung file"):
            try:
                preview_content = uploaded_file.read().decode("utf-8")
                st.text(preview_content)
                uploaded_file.seek(0)  # Reset file pointer
            except:
                st.error("Không thể đọc file. Vui lòng kiểm tra định dạng file.")
        
        # Nút cập nhật danh sách users
        if st.button("🔄 Cập nhật danh sách users"):
            new_users_list = process_uploaded_file(uploaded_file)
            if new_users_list:
                if save_users(new_users_list):
                    st.success(f"✅ Đã cập nhật danh sách users thành công! ({len(new_users_list)} users)")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ Lỗi khi lưu file users!")
            else:
                st.error("❌ Không thể xử lý file được tải lên!")
    
    # Phần đăng nhập
    st.markdown("---")
    st.subheader("🔐 Đăng nhập")
    username = st.text_input("Nhập tên người dùng:")

    if st.button("Đăng nhập"):
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.show_greeting = False # Đảm bảo không hiển thị trang chào mừng
                st.rerun()
            else:
                # Nếu user không hợp lệ, hiển thị trang chào hỏi
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Vui lòng nhập tên người dùng!")

def factorial_calculator():
    """Trang tính giai thừa"""
    st.title("Factorial Calculator")

    # Hiển thị thông tin user đã đăng nhập
    st.write(f"Xin chào, {st.session_state.username}!")

    # Nút đăng xuất
    if st.button("Đăng xuất"):
        # Reset tất cả các session state
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.show_greeting = False
        st.rerun()

    st.divider()

    # Chức năng tính giai thừa
    number = st.number_input("Nhập vào một số:", min_value=0, max_value=900, step=1)

    if st.button("Tính giai thừa"):
        with st.spinner('Đang tính toán...'):
            result = fact(number)
            st.success(f"Giai thừa của {number} là: **{result}**")


def greeting_page():
    """Trang chào hỏi cho user không hợp lệ"""
    st.title("Xin chào!")
    st.write(f"Xin chào {st.session_state.username}!")
    st.error("Bạn không có quyền truy cập vào chức năng tính giai thừa.")
    st.info("Vui lòng sử dụng tài khoản được cấp phép.")

    if st.button("Quay lại đăng nhập"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def main():
    # Khởi tạo các biến trạng thái trong session
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False

    # Điều hướng trang dựa trên trạng thái đăng nhập
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()

if __name__ == '__main__':
    main()
