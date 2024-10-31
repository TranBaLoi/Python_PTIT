class Student:
    def __init__(self, name, *s) -> None:
        self.name = name
        self.correct = int(s[0])
        self.submit = int(s[1])
    
    def __str__(self) -> str:
        return self.name + " " + str(self.correct) + " " + str(self.submit)
    

lst = []
for t in range(int(input())):
    lst += [Student(input(), *input().split())]

lst.sort(key=lambda x : (-x.correct, x.submit, x.name))
print(*lst, sep="\n")

