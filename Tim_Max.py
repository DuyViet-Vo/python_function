def timMax(a,b,c):
    max= a
    if max<b:  max=b
    if max<c: max=c
    return max
a= int(input('nhập a: '))
b= int(input('nhập b: '))
c= int(input('nhập c: '))
print('số lớn nhất là : ',timMax(a,b,c))