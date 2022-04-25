from locale import ABDAY_1


inp = int(input())
## 二分法
# lower = 0
# upper = inp
# middle = (lower + upper) / 2
# while (middle**2 - inp)**2 > 1e-8:
#     if middle**2 - inp > 0:
#         upper = middle
#     else:
#         lower = middle
#     middle = (lower + upper) / 2
# print(str(middle)[0:6])  

# 梯度下降法
# x = 1
# lr = 1e-4
# while (x**2 - inp)**2 > 1e-8:
#     grad = 2 * x
#     if x**2 - inp > 0:
#         x = x - lr * grad
#     else:
#         x = x + lr * grad
# print(str(x)[0:6])

# newton迭代法
x = 1
lr = 1e-4
while (x**2 - inp)**2 > 1e-8:
    grad = 2 * x
    f = (x**2 - inp)
    x = x - f / grad
print(str(x)[0:6])