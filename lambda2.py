def myfunc(n):
    return lambda a: a * n


# Biến mydoubler lúc này sẽ là một lambda function
mydoubler = myfunc(2)

# Vì vậy bạn có thể gọi thoải mái và nhiều lần ở nhièu vị trí
# Và vẫn kế thừa giá trị n của hàm myfunc
print(mydoubler(11))  # Kết quả 22
print(mydoubler(10))  # Kết quả 20
