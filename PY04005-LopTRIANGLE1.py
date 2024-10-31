from math import sqrt

class Point:
    def __init__(point, p1, p2):
        point.x = p1
        point.y = p2
    def distance(point, other):
        return sqrt(pow(point.x-other.x,2) + pow(point.y-other.y,2))

class Triangle:
    def __init__(self, P1, P2, P3) -> None:
        self.x = P1
        self.y = P2
        self.z = P3
    def solve(self):
        a = self.x.distance(self.y)
        b = self.x.distance(self.z)
        c = self.y.distance(self.z)
        return 'INVALID' if max(a,b,c) * 2 >= a + b + c else '{:.3f}'.format(a + b + c)
    

arr = []
t, i = int(input()), 0
for _ in range(t):
    arr += [float(i) for i in input().split()]

for _ in range(t):
    print(Triangle(Point(arr[i+0], arr[i+1]), Point(arr[i+2], arr[i+3]), Point(arr[i+4], arr[i+5])).solve())
    i += 6
