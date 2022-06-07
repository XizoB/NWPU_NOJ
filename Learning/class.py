class Student: # 类
    pass

stu_1 = Student() # 实例 （实例化对象）
print("1:", Student)
print("2:", Student.__name__)
print("3:", Student.__class__)

print("4:", stu_1)
print("5:", stu_1.__class__)

# 动态添加 实例.属性=值
print("6:", stu_1.__dict__)
stu_1.age = 18 # 属性
print("7:", stu_1.__dict__)
print("8:", stu_1.age)

class Student2:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

stu_2 = Student2("Bob", 18)
print("9:", stu_2.age)
print("10:", stu_2.__dict__)
stu_2.age = 20
stu_2.program = ['C','C++']
stu_2.program.append('python')
print("11:", stu_2.__dict__)

stu_2.program = ['C','C++','Java']
print("12:", stu_2.program, id(stu_2.program))
stu_2.program.append('python')
print("13:", stu_2.program, id(stu_2.program))

# 增加类属性 类名.类属性=值
stu_3 = Student2("Marry", 26)
Student2.grade = 1
print("14:", Student2.grade)
print("15:", Student2.__dict__)
print("16:", stu_3.__dict__)
print(stu_3.grade)
stu_3.grade = 3
print("16.1:", stu_3.__dict__)
print(stu_3.grade)
print("17:", Student2.__name__)
print("18:", Student2.__class__)
print("19:", Student2.__module__)

