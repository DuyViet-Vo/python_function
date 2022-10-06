# Chương trình lấy những số chẵn
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Hàm lambda sẽ trả về True nếu là số chẵn, False nếu là số lẻ
new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)
# kết quả là số chẵn
