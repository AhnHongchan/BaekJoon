import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
ground = [[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    ground[x][y] = 1

turn = []
L = int(sys.stdin.readline())
for _ in range(L):
    s, direction = sys.stdin.readline().split()
    s = int(s)
    turn.append((s, direction))

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

stack = deque([(1,1)])

crt = 0
cnt = 0
idx = 0

while True:
    cnt += 1

    head_x, head_y = stack[-1]
    next_x, next_y = head_x + dir[crt][0], head_y + dir[crt][1]
    if next_x < 1 or next_x > N or next_y < 1 or next_y > N or (next_x, next_y) in stack:
        break

    stack.append((next_x, next_y))
    
    if ground[next_x][next_y] == 0:
        stack.popleft()

    else:
        ground[next_x][next_y] = 0
    
    if idx < L and cnt == turn[idx][0]:
        if turn[idx][1] == 'L':
            crt = (crt-1) % 4
        else:
            crt = (crt+1) % 4
        idx += 1

print(cnt)

    