N = int(input())
i = 1
while i:
    if N > 3 *(i**2) -3*i + 1:
        i += 1
    else:
        ans = i
        break
print(ans)