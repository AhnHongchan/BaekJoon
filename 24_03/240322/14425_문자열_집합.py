import sys
input = sys.stdin.readline
N, M = map(int, input().split())
test = []
for _ in range(N):
    test.append(input().rstrip())

cnt = 0
for _ in range(M):
    a = input().rstrip()
    if a in test:
        cnt += 1

print(cnt)