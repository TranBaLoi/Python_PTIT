class Gamer:
    def __init__(self, id, name, timeIn, timeOut):
        self.id = id
        self.name = name
        self.timeOut = timeOut
        self.timeIn = timeIn
        i = int(self.timeIn[0:2])*60 + int(self.timeIn[3:])
        o = int(self.timeOut[0:2])* 60 + int(self.timeOut[3:])
        self.time = o - i
    def Time(self):
        return '{} gio {} phut'.format(self.time // 60 , self.time % 60)
    
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.Time())
    
lst = []
for t in range(int(input())):
    lst.append(Gamer(input(), input(), input(), input()))

lst.sort(key=lambda x : -x.time)
print(*lst, sep='\n')
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00