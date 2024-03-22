import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    info = list(input().split())
    info[0] = int(info[0])
    lst.append(info)
lst.sort(key = lambda x:x[0])

for x in lst:
    print(x[0], x[1])