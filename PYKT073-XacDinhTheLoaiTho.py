res = [len(input().split()) for i in range(int(input()))]
cnt = 0
i , lst = 0, []
while i < len(res):
    if res[i] == 6:
        cnt += 1
        lst.append(1)
        i += 2
        while i < len(res) and res[i] == 6:
            i += 2
    elif res[i] == 7:
        cnt += 1
        lst.append(2)
        i += 4

print(cnt, *lst, sep='\n')
# 8
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay