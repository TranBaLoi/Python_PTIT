class Student:
    def __init__(self, id, name, *s) -> None:
        self.id = 'HS{:02d}'.format(id)
        self.name = name
        sum = 0
        for i in range(len(s)):
            if(i == 0 or i == 1): sum += float(s[i]) * 2
            else:
                sum += float(s[i])
        self.gpa = float(sum / 10 / 1.2)
        if self.gpa < 5:
            self.rank = 'YEU'
        elif self.gpa >=5 and self.gpa <= 6.9:
            self.rank = 'TB'
        elif self.gpa >=7 and self.gpa <= 7.9:
            self.rank = 'KHA'
        elif self.gpa >=8 and self.gpa <= 8.9:
            self.rank = 'GIOI'
        else :
            self.rank = 'XUAT SAC'
    
    def __str__(self) -> str:
        return '{:s} {:s} {:.1f} {:s}'.format(self.id, self.name, self.gpa, self.rank)
    
lst = []
for t in range(1, int(input()) + 1):
    student = Student(t, input(), *input().split())
    lst.append(student)

lst.sort(key=lambda x : (-x.gpa, x.id))
print(*lst, sep='\n')