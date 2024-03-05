N = int(input())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if 0 <= i < 100 and 0 <= j < 100:
                arr[i][j] = 1
            else:
                break

cnt = 0
for lst in arr:
    for x in lst:
        if x == 1:
            cnt += 1

print(cnt)