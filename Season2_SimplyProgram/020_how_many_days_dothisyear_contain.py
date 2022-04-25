inpt = int(input())
if inpt % 100 == 0:
    if inpt % 400 == 0:
        print("366")
    else:
        print("365")
else:
    if inpt % 4 == 0:
        print("366")
    else:
        print("365")