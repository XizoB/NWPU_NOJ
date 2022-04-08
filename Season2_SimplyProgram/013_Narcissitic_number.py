for i in range(100,999):
    a = i % 10
    b = int((i % 100 - a)/10)
    c = int((i - b *10 - a)/100)
    while i == a ** 3 + b ** 3 + c ** 3:
        print(i)
        break