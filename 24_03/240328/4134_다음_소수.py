def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        # 소수 판정 시 n의 제곱근까지만 하는 이유는
        # n = a * b = root(n) ** 2이라고 하면
        # min(a, b) <= root(n)이기 때문이다.
        if x % i == 0:
            return False
    return True

import sys, math
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    while True:
        if prime(n):
            print(n)
            break
        else:
            n += 1