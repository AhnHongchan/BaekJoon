import sys
input = sys.stdin.readline
n = int(input())
dic={}
for _ in range(n):
    arr = list(input().split())

    if arr[1] == 'enter':
        dic[arr[0]] = 1
    else:
        dic[arr[0]] = 0
ans = []
for key, val in dic.items():
    if val == 1:
        ans.append(key)
ans.sort(reverse= True)
print(*ans, sep="\n")