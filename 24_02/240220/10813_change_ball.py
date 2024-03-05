N, M = map(int, input().split())
box = [a for a in range(N+1)]
for x in range(M):
    i, j = map(int, input().split())
    box[i], box[j] = box[j], box[i]

print(*box[1:])
