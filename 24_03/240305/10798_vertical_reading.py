arr = [list(input()) for _ in range(5)]
length = []
for lst in arr:
    length.append(len(lst))

new_lst = ''
for y in range(max(length)):
    for x in range(5):
        if y < length[x]:
            new_lst += arr[x][y]

print(new_lst)