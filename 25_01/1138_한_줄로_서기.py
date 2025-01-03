from itertools import permutations

n = int(input())
clues = list(map(int, input().split()))

numbers = [i for i in range(1, n + 1)]

# 최적화된 탐색
for candidate in permutations(numbers):
    counts = [0] * n
    valid = True  # 유효성 플래그
    
    for i in range(n):
        for j in range(i):
            if candidate[j] > candidate[i]:
                counts[candidate[i] - 1] += 1
        
        # 조기 종료 조건
        if counts[candidate[i] - 1] != clues[candidate[i] - 1]:
            valid = False
            break
    
    if valid and counts == clues:
        print(*candidate)
        break
