import sys
from collections import deque
def BFS():
    while box:
        z, x, y = box.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    box.append((nz,nx,ny))



M, N, H = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [1, 0 , -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
box = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                box.append((i, j, k))

BFS()

impossible = False
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                impossible = True
            day = max(day, arr[i][j][k])

if impossible:
    print(-1)
else:
    print(day-1)
