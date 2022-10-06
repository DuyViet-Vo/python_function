def ChiaHetCho7(number):
    if (number % 7 == 0):
        return True
    else:
        return False


for i in range(1, 100):
    if ChiaHetCho7(i) == True:
        print(i, end=" ")
