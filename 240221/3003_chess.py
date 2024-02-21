white = list(map(int, input().split()))
black = [1, 1, 2, 2, 2, 8]
rest = [0] * 6

for i in range(6):
    rest[i] = black[i] - white[i]

print(*rest)