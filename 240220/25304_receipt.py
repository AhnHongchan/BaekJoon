total = int(input())
n = int(input())
y = 0
for _ in range(n):
    price, num = map(int, input().split())
    x = price * num
    y += x

if total == y:
    print('Yes')
else:
    print('No')