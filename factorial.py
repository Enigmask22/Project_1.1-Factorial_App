# Factorial function
def fact(n):
    """
    Hàm tính giai thừa của một số nguyên không âm.
    Sử dụng vòng lặp để tránh lỗi đệ quy với số lớn.
    """
    if n < 0:
        return "Không xác định" # Giai thừa không xác định cho số âm
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
