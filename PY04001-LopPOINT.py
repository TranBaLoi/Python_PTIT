from math import sqrt

class Point:
    def __init__(point, p1, p2):
        point.x = p1
        point.y = p2
    def distance(point, other):
        return '{:.4f}'.format(sqrt(pow(point.x-other.x,2) + pow(point.y-other.y,2)))
    
def Decimal(x):
    return float(x)



if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1