def nhapDiem():
    toan = float(input("nhập điểm toán: "))
    ly = float(input("nhập điểm lý: "))
    hoa= float(input("nhập điểm hoá: "))
    van = float(input("nhập điểm van: "))
    anh = float(input("nhập điểm anh: "))
    return (toan+ly+hoa+van+anh)/5

def xepLoai(diemTrungBinh):
    if diemTrungBinh<5:
        print('học sinh yếu')
    elif diemTrungBinh<6.9:
        print('học sinh trung bình')
    elif diemTrungBinh<9:
        print('học sinh khá')
    else:
        print('học sinh giỏi')
    print('điểm trung bình là: ',diemTrungBinh)
        
a= nhapDiem()

xepLoai(a)
