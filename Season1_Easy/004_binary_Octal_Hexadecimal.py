binary = int(input(),2)
Octal = int(input(),8)
Decimal = int(input())
Hexadecimal = int(input(),16)
M = max(binary, Octal, Decimal, Hexadecimal)
print("{},{},{},{}".format(bin(M), oct(M), int(M), hex(M)))
