txt = input()
n = len(txt)

if n % 2 == 1:
    if txt[:n//2] == txt[n-1:n//2:-1]:
        print(1)
    else:
        print(0)
else:
    if txt[:n//2] == txt[n-1:n//2-1:-1]:
        print(1)
    else:
        print(0)