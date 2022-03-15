all = int(input())
a = [input() for i in range(all)]
string2 = ","
for i in range(all):
    b = a[i][::-1]
    if b == a[i]:
        a[i] = "True"
    else:
        a[i] = "False"
print(string2.join(a))