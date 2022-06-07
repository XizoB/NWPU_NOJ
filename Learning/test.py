from privatization import Person1, Teacher1

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