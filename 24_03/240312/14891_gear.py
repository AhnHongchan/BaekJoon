from collections import deque
import sys

# direction이 1이면 시계 방향, -1이면 반시계 방향으로 기어를 회전시킨다.
def gear_rotate(gear, direction):
    if direction == 1:
        a = deq[gear].pop()
        deq[gear].appendleft(a)
        return deq
    else:
        b = deq[gear].popleft()
        deq[gear].append(b)
        return deq

'''
내 기어가 돌아가는 전제 하에
나의 9시 방향 자석과 왼쪽의 3시 방향 자석이 일치하지 않을 때
반대 방향으로 왼쪽 기어가 돌아간다.
반면 자석끼리 일치할 경우 회전은 멈추고 그대로 함수가 종료한다.
기어가 회전하기 전 초기값을 기준으로 행동한다.
'''
def left(gear, direction):
    if 1 <= gear <= 3:
        if deq[gear][6] != deq[gear-1][2]:
            if direction:
                left(gear-1, -direction)
                gear_rotate(gear-1, -direction)

'''
내 기어가 돌아간다는 전제 하에
나의 3시 방향 자석과 오른쪽의 6시 방향 자석이 일치하지 않을 때
반대 방향으로 오른쪽 기어가 돌아간다.
반면 자석끼리 일치할 경우 회전은 멈추고 그대로 함수가 종료한다.
기어가 회전하기 전 초기값을 기준으로 행동한다.
'''

def right(gear, direction):
    if 0 <= gear <= 2:
        if deq[gear][2] != deq[gear+1][6]:
            if direction:
                right(gear+1, -direction)
                gear_rotate(gear+1, -direction)
    return deq

# 덱으로 주어진 기어들을 받음: 회전 시 시간 복잡도를 줄이기 위해
deq = deque(deque(sys.stdin.readline().strip()) for _ in range(4))
N = int(sys.stdin.readline())

# 주어진 만큼 회전을 돈다.
for _ in range(N):
    gear, direction = list(map(int, sys.stdin.readline().split()))
    gear -= 1
    left(gear, direction)
    right(gear, direction)
    gear_rotate(gear, direction)

# 회전을 마치고 12시의 값이 0이면 0점, 1이면 2 ** i만큼 더해준다.
cnt = 0
for i in range(4):
    if deq[i][0] == '1':
        cnt += 2 ** i

print(cnt)

'''
코드길이: 1077B
Python 3 기준
메모리: 34.088MB, 시간: 64ms
PyPy 3 기준
메모리: 112.004MB, 시간: 140ms
'''