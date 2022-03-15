num = int(input())
a = [input() for i in range(num)]
strings = ','
SYMBOL_VALUES = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}

def romanToint(s:str) -> int:
    count = len(s)
    end = []
    for i in range(count):
        ans = 0
        length = len(a[i])
        for j in range(length):
            item = a[i][j]
            value = SYMBOL_VALUES[item]
            if j < length - 1 and value < SYMBOL_VALUES[a[i][j + 1]]:
                ans -= value
            else:
                ans += value
        end.append(str(ans))
    return end
print(strings.join(romanToint(a)))
# 3
# MMXXI        
# MMMCMXCIX
# CMXLIX