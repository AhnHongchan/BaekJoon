n = int(input())
lst = list(map(int, input().split()))

min_val = 1000000
max_val = -1000000

for i in range(n):
    if lst[i] > max_val:
        max_val = lst[i]
    if lst[i] < min_val:
        min_val = lst[i]

print(min_val, max_val)