txt = input()
abc = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum_val = 0

for x in txt:
    for j in range(8):
        if x in abc[j]:
            sum_val += j+3

print(sum_val)



