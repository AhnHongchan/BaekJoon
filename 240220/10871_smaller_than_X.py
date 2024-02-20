N, X = map(int, input().split())
lst = list(map(int, input().split()))

for elem in lst:
    if elem < X:
        print(elem, end=' ')