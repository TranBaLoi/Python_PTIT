class ThiSinh:
    def __init__(self, name, birth, d1, d2, d3) -> None:
        self.name = name
        self.birth = birth
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def __str__(self) -> str:
        return (self.name + " " + self.birth + " " +
                "{:.1f}".format(self.d1 + self.d2 + self.d3))

print(ThiSinh(input(), input(), float(input()), float(input()), float(input())))