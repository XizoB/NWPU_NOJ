def addition2(count):
    def counting():
        nonlocal count
        count += 1
        return count
    return counting
a = addition2(0)
print(a())
print(a())
print(a())
print(a())
print(a())
