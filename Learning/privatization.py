"""公有属性"""
from sympy import per


class Person:
    a = 1 
    def test(self):
        print(Person.a)
        print(self.a)

class Teacher(Person):
    def test1(self):
        print(Teacher.a)
        print(self.a)

# 测试类内部能否访问
P = Person()
P.test()

# 测试类外部（子类内部）能否访问
t = Teacher()
t.test1()

# 测试当前模块内能否访问
print("1:", Person.a)
print("2:", Teacher.a)
print("3:", P.a)
print("4:", t.a)

"""私有化属性"""
class Person1:
    _a = 1
    def test(self):
        print(Person1._a)
        print(self._a)

class Teacher1(Person1):
    def test1(self):
        print(Teacher1._a)
        print(self._a)

# 测试类内部能否访问
p = Person1()
p.test()
# 测试类外部（子类内部）能否访问
t = Teacher1()
t.test1()

# 测试当前模块内能否访问
print("5:", Person1._a)
print("6:", Teacher1._a)
print("7:", p._a)
print("8:", t._a)
print(Teacher1.__dict__)
print(Person1.__dict__)



"""私有化中的私有化属性"""
class Person2:
    __a = 1
    def test(self):
        print(Person2.__a)
        print(self.__a)
class Teacher2(Person2):
    def test1(self):
        print(Teacher2.__a)
        print(self.__a)

# 测试类内部能否访问
p = Person2()
p.test()
# 测试类外部（子类内部）能否访问
# t = Teacher2()
# t.test1()

# 测试当前模块内能否访问
# print(Person2.__a) # 报错
# print(Teacher2.__a) # 报错
# print(p.__a)
# print(t.__a)

print(Person2.__dict__)

class User:
    def __init__(self):
        self.usr = "admin"
        self.__password = 123456

usr1 = User()
#print(usr1.__password)
usr1.__password = 654321
print(usr1.__password)
print(usr1.__dict__)

class User1:
    def __init__(self):
        self.usr = "admin"
        self.__password = 123456
    @property
    def password(self):
        return self.__password

usr1 = User1()
print(usr1.password)
print(usr1.__dict__)

class User2:
    def __init__(self):
        self.__name = "admin"

    @property
    def name(self):
        print("获取用户名")
        return self.__name

    @name.setter
    def name(self, new):
        print("重置用户名")
        self.__name = new

usr2 = User2()
print(usr2.name)
usr2.name = 'xyh'
print(usr2.name)
print(usr2.__dict__)

class Animal:
    print("2")
class Human:
    pass
class Teacher(Human):
    __metaclass__ = Animal

print(Teacher.__metaclass__)