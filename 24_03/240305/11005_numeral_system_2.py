N, B = map(int, input().split())
txt = ''
while N:
    if N % B >= 10:
        txt += chr(N%B+55)
    elif N % B < 10:
        txt += str(N%B)
    
    N = N // B

print(txt[::-1])