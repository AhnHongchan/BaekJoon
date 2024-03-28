import sys

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

input = sys.stdin.readline
N = int(input())
lst = []
first = int(input())
for i in range(N-1):
    num = int(input())
    lst.append(num - first)
    first = num

gap = lst[0]
for i in range(1, len(lst)):
    gap = GCD(gap, lst[i])

cnt = 0
for x in lst:
    cnt += x // gap - 1
print(cnt)