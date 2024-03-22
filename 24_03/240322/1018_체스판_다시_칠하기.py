def cnt_paint(arr, x, y):
    cnt = 0
    start_color = arr[x][y]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if arr[x+i][y+j] != start_color:
                    cnt += 1
            else:
                if arr[x+i][y+j] == start_color:
                    cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

min_cnt = float('inf')

for x in range(N-7):
    for y in range(M-7):
        # 스타트 색깔 자체를 바꾸는 게 더 나은 경우가 있기 때문에 64-cnt_paint를 해 준 것
        min_cnt = min(min_cnt, cnt_paint(arr, x, y), 64 - cnt_paint(arr, x, y))

print(min_cnt)
