class NhanVien:
    def __init__(self, id, name, lt, th):
        self.id = "TS0{}".format(id)
        self.name = name
        if lt > 10:
            lt /= 10
        if th > 10:
            th /= 10
        self.gpa = (lt + th) / 2
        if self.gpa > 9.5:
            self.rank = "XUAT SAC"
        elif self.gpa >= 8 and self.gpa <= 9.5:
            self.rank = "DAT"
        elif self.gpa >= 5 and self.gpa < 8:
            self.rank = "CAN NHAC"
        else:
            self.rank = "TRUOT"
    def __str__(self):
        return '{:s} {:s} {:.2f} {:s}'.format(self.id, self.name, self.gpa, self.rank)

lst = []    
for t in range(int(input())):
    lst.append(NhanVien(t+1, input(), float(input()), float(input())))

lst.sort(key=lambda x : -x.gpa)
print(*lst, sep='\n')
