import sys

def knapsack(N, K, weights, values):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, K + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[N][K]



N, K = map(int, sys.stdin.readline().split())
weight = []
value = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    weight.append(W)
    value.append(V)

result = knapsack(N, K, weight, value)
print(result)



