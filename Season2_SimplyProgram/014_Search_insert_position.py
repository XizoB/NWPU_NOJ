inp = input().split(',')
val = int(input())
for i in range(len(inp)):
    if int(inp[i]) - val == 0:
        print(i)
        break
    elif val - int(inp[i]) > 0:
        if i < len(inp) - 1:
            if val - int(inp[i+1]) < 0:
                print(i+1)
                break
        else:
            print(i+1)
            break
    else:
        print(i)
        break
