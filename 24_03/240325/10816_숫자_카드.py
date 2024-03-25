import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr_2 = list(map(int, input().split()))
dic = {}

for x in arr:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for y in arr_2:
    if y in dic:
        print(dic[y], end=" ")
    else:
        print(0, end=" ")