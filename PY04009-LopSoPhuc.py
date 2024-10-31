class SoPhuc:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def sum(self, A):
        C = SoPhuc(0, 0)
        C.a = A.a + self.a
        C.b = A.b + self.b
        return C
    
    def mul(self, A):
        C = SoPhuc(0, 0)
        C.a = self.a*A.a + self.b*A.b*(-1)
        C.b = self.a*A.b + self.b*A.a
        return C
    
    def __str__(self) -> str:
        return (str(self.a) + (" + " + str(self.b) if self.b >= 0
                else ' - ' + str(abs(self.b))) + 'i')
for t in range(int(input())):
    tmp = [int(i) for i in input().split()]
    A = SoPhuc(tmp[0], tmp[1])
    B = SoPhuc(tmp[2], tmp[3])
    tmp = A.sum(B)
    C = tmp.mul(A)
    D = tmp.mul(tmp)
    print("{}, {}".format(C, D))

