print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# khởi tạo biến tổng (phải đặt ngoài vòng lặp)
total_budget = 0

# vòng lặp nhập lương 3 nhân viên
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)

    # nhập lương từng nhân viên
    salary = int(input("Nhập mức lương (VNĐ): "))

    # cộng dồn vào tổng
    total_budget = total_budget + salary

# in kết quả cuối cùng
print("KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")
#lỗi
# total_budget được khởi tạo bên trong vòng lặp,
# nên mỗi lần lặp giá trị lại bị reset về 0.
# Vì vậy chương trình chỉ giữ lương của nhân viên cuối cùng
# thay vì cộng dồn tất cả nhân viên.
#Sửa đúng
#total_budget đƯợc khởi tạo bên ngoài vòng lặp
#nên mỗi lần lặp giá trị nó sẽ không reset về 0
#vì vậy chương trình sẽ cộng tổng của mức luong nhân viên cuối cùng

