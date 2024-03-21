cycle = True
while cycle:
    A, B = map(int, input().split())
    if A == 0 or B == 0:
        break
    if A % B == 0:
        print('multiple')
    elif B % A == 0:
        print('factor')
    else:
        print('neither')