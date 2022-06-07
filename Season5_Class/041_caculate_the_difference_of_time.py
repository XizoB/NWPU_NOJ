starttime = input().split()
endtime = input().split()
def caculatedays(starttime, endtime):
    syear, eyear = int(starttime[0]), int(endtime[0])
    smonth, emonth = int(starttime[1]), int(endtime[1])
    sday, eday = int(starttime[2]), int(endtime[2])
    if any([syear % 100 == 0 and syear % 400 == 0, syear % 100 != 0 and syear % 4 == 0]):
            print("366")
    else:
            print("365")