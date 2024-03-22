import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in range(N):
    dic[arr[i]] = 1

M = int(input())
arr_2 = list(map(int, input().split()))

for i in range(M):
    if arr_2[i] in dic:
        print(dic[arr_2[i]], end=" ")
    else:
        print(0, end=" ")