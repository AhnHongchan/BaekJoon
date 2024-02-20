lst = [0] * 42
for _ in range(10):
    num = int(input())
    rest = num % 42
    lst[rest] += 1

cnt = 0
for i in range(len(lst)):
    if lst[i] != 0:
        cnt += 1

print(cnt)