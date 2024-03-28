import sys

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

input = sys.stdin.readline

a, b = map(int, input().split())

for i in range(a, b+1):
    if prime(i):
        print(i)