T = int(input())
for _ in range(T):
    n, txt = input().split()
    n = int(n)
    for x in txt:
        print(x * n, end='')
    print()