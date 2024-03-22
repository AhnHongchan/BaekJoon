import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr_2 = sorted(set(arr))
dic = {}
for i in range(len(arr_2)):
    dic[arr_2[i]] = i

for x in arr:
    print(dic[x], end=" ")