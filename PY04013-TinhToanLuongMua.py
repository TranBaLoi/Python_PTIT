from datetime import *
class Data:
    def __init__(self, id, name, start, end, amout) -> None:
        self.id = 'T{:02d}'.format(id)
        self.name = name
        self.time = datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")
        self.amout = amout

    def __str__(self) -> str:
        return (self.id + ' ' + self.name + ' ' + 
        '{:.2f}'.format(self.amout * 3600 / self.time.seconds))
    
lst = []
def isValue(data):
    for i in lst:
        if i.name == data.name:
            i.time += data.time
            i.amout += data.amout
            return
    lst.append(data)

for t in range(1, int(input()) + 1):
    data = Data(t, input(), input(), input(), int(input()))
    isValue(data)

print(*lst, sep='\n')