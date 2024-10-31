from math import gcd

class PhanSo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def solve(self):
        k = gcd(self.x, self.y)
        return '{}/{}'.format(self.x // k, self.y // k)
    
x, y = [int(i) for i in input().split()]
p = PhanSo(x, y)
print(p.solve())