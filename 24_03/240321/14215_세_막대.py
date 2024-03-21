a, b, c = map(int,input().split())
if a + b + c > 2 * max(a, b, c):
    print(a+b+c)
else:
    print(2*(a+b+c - max(a, b, c))-1)
