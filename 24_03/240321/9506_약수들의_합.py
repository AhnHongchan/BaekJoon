while True:
    N = int(input())
    if N == -1:
        break
    sum_v = 0
    sum_lst = []
    for i in range(1, N):
        if N % i == 0:
            sum_v += i
            sum_lst.append(i)
            sum_lst.append('+')
    if N == sum_v:
        sum_lst.pop()
        print(f'{N} =', *sum_lst)
    else:
        print(f'{N} is NOT perfect.')
