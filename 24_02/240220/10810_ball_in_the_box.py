N, M = map(int, input().split())
box = [0] * (N+1)
for i in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        box[x] = k

print(*box[1:])