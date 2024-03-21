N, K = map(int, input().split())
cnt = 0
cycle = True
while cycle:
    for i in range(1, N+1):
        if N % i == 0:
            cnt += 1
        if cnt == K:
            ans = i
            cycle = False
            break
    if cnt < K:
        ans = 0
        cycle = False

print(ans)