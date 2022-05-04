a = '1'
b = '2'
print(a + b)

def f(a, b, c):
    print(a, b, c, sep="~")
f(1,2,3)
# 1~2~3
list1 = [1,2,3]
print(*list1)
f(*list1)

def f(**kwargs):
    print(kwargs)
dict1 = {'a':1,'b':2,'c':3}
print(*dict1)
f(**dict1)

def outer():
    x = 5
    print(10*x)
    def inner():
        print(x)
    return inner()
outer()

def decorator(func):
    def my_name():
        print('My name is', end=' ')
        return func
    return my_name()

@decorator
def name():
    print("Bob")

# print_name = decorator(name)
# print_name()
name()

def f(x):
    return x**2
def square_list(f,s):
    result = []
    for item in s:
        i = f(item)
        result.append(i)
    return result
s = [1,2,3,4,5]
#t = square_list(f,s)
t = square_list(lambda x: x**2, s)
print(t)

import random
random_lambda = lambda: random.random()
print(random_lambda())

a = "1"
b = "*"
c = "2"
print(eval(a+b+c))
print(int(3.2))
a = [1, 2, 3]
print(*a)

a = ["1","2"]
print(a.index("3"))