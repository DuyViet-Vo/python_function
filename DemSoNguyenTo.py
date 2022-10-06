def la_SNT(n):
    if (n < 2):
        return False
    elif (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    else:
        # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
        for i in range(3, n, 2):
            if (n % i == 0):
                return False
    return True


counter = 0

for i in range(1, 101):
    if la_SNT(i):
        counter += 1
        print(i, end=' ')
print("______________")
print("Tổng SNT trong phạm vi này là: ", counter)
