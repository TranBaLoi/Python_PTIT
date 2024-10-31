for t in range(int(input())):
    n = input()
    mul = 1
    for i in range(1,10):
        mul *= i ** n.count(str(i))
    print(mul)