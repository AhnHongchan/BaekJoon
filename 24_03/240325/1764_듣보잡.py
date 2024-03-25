import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
for _ in range(N+M):
    a = input().rstrip()
    if a in dic:
        dic[a] = 2
    else:
        dic[a] = 1

cnt = 0
lst = []
for key, val in dic.items():
    if val == 2:
        cnt += 1
        lst.append(key)
lst.sort()
print(cnt)
for x in lst:
    print(x)