num = int(input())
num2 = input().split()
num3 = [[int(num2[2*i]),int(num2[2*i+1])] for i in range(int(len(num2)/2))]
print(num3)
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])
    output = [str(merged[i][j]) for i in range(len(merged)) for j in range(2)]
    output = " ".join(output)
    #print(*merged)
    #return output
print(merge(num3))
#1 3 2 6 8 10 15 18