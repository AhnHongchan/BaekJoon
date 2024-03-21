N = int(input())
arr = list(map(int, input().split()))
prime_num = 0
for i in range(N):
    cnt = 0
    for x in range(1, arr[i]+1):
        if arr[i] % x == 0:
            cnt += 1
    if cnt == 2:
        prime_num += 1

print(prime_num)