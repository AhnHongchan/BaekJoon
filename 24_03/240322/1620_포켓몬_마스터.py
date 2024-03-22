import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic={}
for i in range(1, N+1):
    dic[input()] = str(i)

for _ in range(M):
    a = input().rstrip()
    if not a.isdigit():
        print(int(dic[a]))
    else:
        for key, val in dic.items():
            if val == a:
                print(key)