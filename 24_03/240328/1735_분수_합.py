import sys

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())

son = a * d + b * c
parent = b * d

e = GCD(son, parent)
son //= e
parent //= e
print(son, parent)