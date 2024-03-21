import math

A, B, V = map(int, input().split())

run = A - B
day = math.ceil((V-A)/run)
day += 1
print(day)