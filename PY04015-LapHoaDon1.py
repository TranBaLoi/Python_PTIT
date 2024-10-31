class Customer:
    def __init__(self, id, name, begin, end) -> None:
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        used = end - begin
        self.money = 0
        if used > 100 :
            self.money = 50 * 100 
            self.money += 50 * 150
            used -= 100
            self.money += used * 200 
            self.money += self.money * 0.05
        elif used > 50 and used <= 100:
            self.money = 50 * 100
            used -= 50
            self.money += used * 150 
            self.money += self.money * 0.03
        else:
            self.money = used * 100 + (used * 100) * 0.02
        self.money = round(self.money)
    def __str__(self) -> str:
        return '{:s} {:s} {:s}'.format(self.id, self.name, str(int(self.money)))
    

lst = []
for t in range(1, int(input())+1):
    lst.append(Customer(t, input(), int(input()), int(input())))

lst.sort(key=lambda x : (-x.money))
print(*lst, sep='\n')