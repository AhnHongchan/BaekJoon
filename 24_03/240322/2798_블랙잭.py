from itertools import combinations

N, M = map(int,input().split())
card = list(map(int, input().split()))
comb = list(combinations(card, 3))
max_v = 0
for i in range(N*(N-1)*(N-2)//6):
    sum_v = comb[i][0] + comb[i][1] + comb[i][2]
    if sum_v == M:
        max_v = M
        break
    elif sum_v < M:
        if max_v < sum_v:
            max_v = sum_v
    else:
        continue

print(max_v)
    