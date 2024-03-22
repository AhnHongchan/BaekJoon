N = int(input())
bk = True
for y in range(1668):
    for x in range(1001):
        if 5*x+3*y > N:
            break
        elif 5*x+3*y == N:
            bk = False
            print(x+y)
            break
    if bk == False:
        break
if bk == True:
    print(-1)