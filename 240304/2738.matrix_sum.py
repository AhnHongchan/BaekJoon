N, M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(2 * N)]
new_arr = [[0] * M for _ in range(N)]

for x in range(N):
    for y in range(M):
        new_arr[x][y] = arr[x][y] + arr[x+N][y]

for lst in new_arr:
    print(*lst)