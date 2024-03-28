import sys, math
input = sys.stdin.readline

T = int(input())

arr = [True for _ in range(1000000 + 1)]
arr[0], arr[1] = False, False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(1000000) + 1)): #2부터 돈다.
    if arr[i]: #만약 array1[i]가 True(소수)라면
        j = 2 #i에 곱해줄 j값을 2부터 설정
        while i * j <= 1000000: #i * j 가 1000000 보다 작거나 같다면
            arr[i * j] = False #해당 i*j의 값은 소수가 아니므로 False로 설정
            j += 1 #j를 1씩 증가


for _ in range(T):
    n = int(input())
    cnt = 0
    for i in range(2,n//2+1):
        if arr[i] and arr[n-i]:
            cnt += 1
    print(cnt)