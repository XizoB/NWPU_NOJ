num = int(input())
def fibonacci(num):
    if num==0:
        out = 0
    elif num==1:
        out = 1
    else:
        older = 0
        old = 1
        for _ in range(num - 1):
            out = old + older
            older = old
            old = out
    return out
print(fibonacci(num))