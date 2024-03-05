T = int(input())
for _ in range(1, T+1):
    money = int(input())
    lst = []
    a = money // 25
    money = money - 25 * a
    lst.append(a)
    b = money // 10
    money = money - 10 * b
    lst.append(b)
    c = money // 5
    money = money - 5 * c
    lst.append(c)
    d = money // 1
    money = money - 1 * d
    lst.append(d)
    print(*lst)