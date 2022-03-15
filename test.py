import decimal
from errno import ELIBBAD
import re

a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = decimal.Decimal('0.3')
print(a + b - c)
print(1/3)
print(decimal.Decimal(1)/decimal.Decimal(3))
decimal.getcontext().prec = 50
print(decimal.Decimal('1')/decimal.Decimal('3'))
print("{0}*{1}={2:0>8}".format(3,2,2*3))
print("{:*^30}".format('center'))
print("{:.3f}".format(3.1415926))
print( ' '.join([str(i) for i in range(5)]))
ans = [i for i in range(5)]
print([i for i in range(5)])
b = "{}{}".format('b',4)
print(b)
a = ['123','245',456]
print(a[1][::-1])
list1 = [1,2,3,4,5]
print(list1[-5:-1])
list3 = [1,2,5,46,8]
list3.sort(reverse=True)
print(list3)

c ={
    'a':1,
    'b':2,
    'c':3,
}
for item in enumerate(c):
    print(item, c[item])