num, kind = input().split()
num = list(num)

for i in range(len(num)):
    if num[i].isdigit():
        num[i] = int(num[i])
    else:
        num[i] = ord(num[i])-55

sum_v = 0
for i in range(len(num)):
    sum_v += num[i] * (int(kind) ** (len(num)-1-i))

print(sum_v)