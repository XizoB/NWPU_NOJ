four = int(input())
second = int(input())
third = int(input())
end = (four + second) % third
end = "{:0>4}".format(end)
transfer = end[::-1]
print(transfer)