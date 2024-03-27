import sys

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    dic = {}
    A, B = map(int, input().split())
    C = GCD(A, B)
    print(A * B // C)