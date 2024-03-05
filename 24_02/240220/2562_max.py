max_val = 0
cnt = 0
for i in range(1,10):
    num = int(input())
    if max_val < num:
        max_val = num
        cnt = i

print(max_val)
print(cnt)