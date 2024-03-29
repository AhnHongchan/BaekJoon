import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = []
    top = -1
    arr = list(input().rstrip())
    for i in range(len(arr)):
        if arr[i] == '(':
            top += 1
            stack.append(arr[i])
        else:
            top -=1
            if top < -1:
                break
            else:
                stack.pop()
    if top == -1:
        print('YES')
    else:
        print('NO')