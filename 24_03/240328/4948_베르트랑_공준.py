import sys, math
input = sys.stdin.readline

cycle = True
arr = [True for _ in range(2*123456 + 1)]
arr[0], arr[1] = False, False

# 에라토스테네스의 체 공식
for i in range(2, int(math.sqrt(2 * 123456) + 1)): #2부터 int(math.sqrt(2 * 123456) 까지 돈다.
    if arr[i]: #만약 array1[i]가 True(소수)라면
        j = 2 #i에 곱해줄 j값을 2부터 설정
        while i * j <= 2 * 123456: #i * j 가 2* 123456 보다 작거나 같다면
            arr[i * j] = False #해당 i*j의 값은 소수가 아니므로 False로 설정
            j += 1 #j를 1씩 증가


while cycle:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if arr[i]:
            cnt += 1
    print(cnt)
