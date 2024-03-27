import sys

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

input = sys.stdin.readline

A, B = map(int, input().split())
C = GCD(A, B)
print(A * B // C)