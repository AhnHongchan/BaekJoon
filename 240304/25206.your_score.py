total = 0
sub = 0
table = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    arr = list(input().split())
    if arr[2] == 'P':
        pass
    else:
        value = table.get(arr[2])
        total += float(arr[1]) * value
        sub += float(arr[1])

print(f'{total/sub:.6f}')