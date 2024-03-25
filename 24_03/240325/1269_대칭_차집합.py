import sys
input = sys.stdin.readline
N, M = map(int, input().split())
left = list(map(int, input().split()))
left += list(map(int, input().split()))
dic = {}
for x in left:
    if x in dic:
        dic[x] = 0
    else:
        dic[x] = 1

cnt = 0
for val in dic.values():
    if val == 1:
        cnt += 1

print(cnt)