while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    if a + b + c <= 2 * max(a, b, c):
        print('Invalid')
    
    elif (a != b) and (b != c) and (c != a):
        print('Scalene')
    
    elif a == b == c:
        print('Equilateral')
    
    else:
        print('Isosceles')