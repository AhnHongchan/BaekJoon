import sys
input = sys.stdin.readline
N = int(input())
stack = []
for i in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        stack.append(arr[1])
    elif arr[0] == 2:
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif arr[0] == 3:
        print(len(stack))
    elif arr[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif arr[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)