#hàm tạo sinh viên
def create_student(name):
    return lambda infor: name +" " + infor

#in ra thông tin sinh viên
name = input("Nhập tên sinh viên: ")

#Khởi tao sinh viên
student = create_student(name)

#in tuổi 
print('nhập tuổi')
print(student(input()))

#in giới tính
print('Nhập giới tính')
print(student(input()))
