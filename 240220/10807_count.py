n = int(input())
lst = list(map(int, input().split()))
num = int(input())
cnt = 0
for i in range(n):
    if lst[i] == num:
        cnt += 1    

print(cnt)
