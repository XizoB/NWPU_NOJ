class Sulotion:
    def __init__(self, arra, num):
        self.arra = arra
        self.num = num
        self.count = 0
        self.temp = [0 for _ in range(self.num)] # 生成临时的全排列num
        self.visit = [True for _ in range(len(self.arra))] # 访问的标记

    def fullarray(self, position):
        # 递归出口
        if position == self.num:
            x, y, z, m, n = 0, 1, 2, 3, 4
            xy = (self.temp[x]*10 + self.temp[y])
            zmn = (self.temp[z]*100 + self.temp[m]*10 + self.temp[n])
            xmy = (self.temp[x]*100 + self.temp[m]*10 + self.temp[y])
            zn = (self.temp[z]*10 + self.temp[n])
            #print(xy, zmn, xmy, zn)
            if xy*zmn == xmy*zn:
                self.count += 1
            return
        # 递归主体
        for index in range(0, len(self.arra)):
            if self.visit[index] == True:
                self.temp[position] = self.arra[index]
                self.visit[index] = False  # 试探 
                Sulotion.fullarray(self, position + 1)
                self.visit[index] = True  # 回溯，非常重要
    
    def returncount(self):
        print(self.count)
    

arra = [i for i in range(1,10)]
num = 5
S = Sulotion(arra, num)
S.fullarray(0)
S.returncount()
