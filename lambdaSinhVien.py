#hàm tạo sinh viên
from numpy import piecewise


def create_student(name):
    return lambda infor: name +" " + infor

#in ra thông tin sinh viên
name = input("Nhập tên sinh viên: ")

#Khởi tao sinh viên
student = create_student(name)

#in tuổi 
print(student(input('nhập tuổi')))

#in giới tính
print(student(input('Nhập giới tính')))

#in quốc tịch
print(student(input('nhập quốc tịch: ')))