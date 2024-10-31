from math import gcd

class PhanSo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def solve(self, other):
        mau = self.y * other.y
        tu = self.x * other.y + self.y * other.x
        k = gcd(tu, mau)
        return '{}/{}'.format(tu // k, mau // k)    
arr = [int(i) for i in input().split()]
p = PhanSo(arr[0], arr[1])
r = PhanSo(arr[2], arr[3])
print(p.solve(r))