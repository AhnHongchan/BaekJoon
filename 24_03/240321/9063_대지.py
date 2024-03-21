from collections import deque
x = deque()
y = deque()
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

width = max(x)-min(x)
height = max(y)-min(y)
print(width * height)