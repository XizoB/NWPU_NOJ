one = complex(input())
two = complex(input())
try:
    plus = one + two
    minus = one - two
    multiply = one * two
    division = one/two
    conjugate = one.conjugate()
    abs = abs(one)
    print("{},{},{},{},{},{}".format(plus, minus, multiply, division, conjugate, abs))
except:
    print('ERROR')