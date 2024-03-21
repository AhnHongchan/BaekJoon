from collections import deque

M = int(input())
N = int(input())
sum_v = deque()
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        sum_v.append(i)

if not sum_v:
    print(-1)
else:
    print(sum(sum_v))
    print(sum_v.popleft())