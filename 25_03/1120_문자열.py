a, b = input().split()

na = len(a)
nb = len(b)

result = float('inf')

for i in range(nb-na+1):
    cnt = 0
    for j in range(na):
        if a[j] != b[i+j]:
            cnt += 1
    
    result = min(result, cnt)

print(result)