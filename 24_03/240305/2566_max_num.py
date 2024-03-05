arr = [list(map(int, input().split())) for _ in range(9)]

max_v = -1
idx_x = 0
idx_y = 0
for x in range(9):
    for y in range(9):
        if max_v < arr[x][y]:
            max_v = arr[x][y]
            idx_x = x + 1
            idx_y = y + 1

print(max_v)
print(idx_x, idx_y)