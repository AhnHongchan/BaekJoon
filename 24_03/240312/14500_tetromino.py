import sys


# 정사각형 합 구하기
def square(x, y):
    sum_v = 0
    if 0 <= x <= N-2 and 0 <= y <= M-2:
        sum_v += (arr[x][y] + arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1])
    return sum_v

# 4칸짜리 1직선 가로 혹은 세로 중에 큰 것 구하기
def long(x, y):
    sum_v1 = 0
    sum_v2 = 0
    if 0 <= x <= N-4:
        sum_v1 += (arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y])

    if 0 <= y <= M-4:
        sum_v2 += (arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x][y+3])
    
    result = max(sum_v1, sum_v2)
    return result

# L자, S자, ㅗ자 중에 2by3 칸에 들어가는 경우 중 가장 큰 것 구하기
def two_by_three(x, y):
    sum_v1 = 0
    sum_v2 = 0
    sum_v3 = 0
    sum_v4 = 0
    sum_v5 = 0
    sum_v6 = 0
    sum_v7 = 0
    sum_v8 = 0
    if 0 <= x <= N-2 and 0 <= y <= M-3:
        sum_v1 += (arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y])
        sum_v2 += (arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+2])
        sum_v3 += (arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2])
        sum_v4 += (arr[x][y+2] + arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2])
        sum_v5 += (arr[x][y+1] + arr[x][y+2] + arr[x+1][y] + arr[x+1][y+1])
        sum_v6 += (arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y+2])
        sum_v7 += (arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1])
        sum_v8 += (arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2] + arr[x][y+1])
    
    result = max(sum_v1, sum_v2, sum_v3, sum_v4, sum_v5, sum_v6, sum_v7, sum_v8)
    return result

# L자, S자, ㅗ자 중에 3by2 칸에 들어가는 경우 중 가장 큰 것 구하기
def three_by_two(x, y):
    sum_v1 = 0
    sum_v2 = 0
    sum_v3 = 0
    sum_v4 = 0
    sum_v5 = 0
    sum_v6 = 0
    sum_v7 = 0
    sum_v8 = 0
    if 0 <= x <= N-3 and 0 <= y <= M-2:
        sum_v1 += (arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+2][y+1])
        sum_v2 += (arr[x+2][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1])
        sum_v3 += (arr[x][y] + arr[x][y+1] + arr[x+1][y] + arr[x+2][y])
        sum_v4 += (arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1])
        sum_v5 += (arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+2][y+1])
        sum_v6 += (arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y] + arr[x+2][y])
        sum_v7 += (arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1])
        sum_v8 += (arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1])

    result = max(sum_v1, sum_v2, sum_v3, sum_v4, sum_v5, sum_v6, sum_v7, sum_v8)
    return result


# 주어진 맵
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 위치마다 가장 큰 값을 가지는 도형을 구하고 그 값을 max_v와 비교하여 더 큰 쪽을 max_v로 놓기
max_v = 0
cur_v = 0
for x in range(N):
    for y in range(M):
        lst = [square(x, y), long(x, y), two_by_three(x, y), three_by_two(x, y)]
        cur_v = max(lst)
        if cur_v > max_v:
            max_v = cur_v

print(max_v)

'''
코드 길이: 2062B
Python3
메모리 길이: 37.708MB, 시간: 1236ms
PyPy3
메모리 길이: 158.552MB, 시간: 1716ms
'''