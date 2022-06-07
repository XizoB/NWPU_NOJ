
# 实例方法
class Student:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print("My name is", self.name)

# 标准调用
stu_1 = Student("Bob")
stu_1.print_name()

# 通过类调用
Student.print_name(stu_1)
func = Student.print_name
func(stu_1)

# 类方法
class Student1:
    @classmethod
    def print_class(cls, name):
        print("My name is", name)

Student1.print_class("Lily")
stu_2 = Student1()
stu_2.print_class("Mia")

# 静态方法
class Student2:
    @staticmethod
    def print_class(name):
        print("My name is", name)
Student2.print_class("Amy")
stu_3 = Student2()
stu_3.print_class("Bob")

"""实例方法，可以访问实例属性，也可以访问类属性"""
class Teacher:
    class_room = 207 # 类属性
    def object_name(self):
        print('This is an object method.')
        print(self.class_room)
        print(self.name) # 实例属性
print("1:", Teacher.__dict__)

teacher1 = Teacher()
teacher1.name = "XYH"
teacher1.object_name()

"""类方法，不能访问实例属性，通过cls来访问类属性""" 
class Teacher1:
    class_room = 207
    @classmethod
    def class_name(cls):
        cls.name = "Bob"
        print("This is a class method.")
        print(cls.class_room)
        print(cls.name)
teacher2 = Teacher1()
teacher2.name = "XYH"
teacher2.class_name()
print("2:", teacher2.__dict__)
print("3:", Teacher1.__dict__)

"""静态方法，不能访问实例属性，直接通过类的名称来访问类属性 """
class Teacher2:
    class_room = 207
    @staticmethod
    def static_name():
        print("This is a static method.")
        print(Teacher2.class_room)
teacher3 = Teacher2()
teacher3.name = "XYH"
Teacher2.static_name()