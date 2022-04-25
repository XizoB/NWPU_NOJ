from math import cos, radians, sin, tan
inpt = int(input())
radian = radians(inpt)
z = sin(radian) + cos(radian) - tan(radian/4)**2
print("%.4f"%radian)
print("%.4f"%z)
