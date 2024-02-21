txt = input()
txt = txt.upper()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = [0] * 26

for i in range(len(txt)):
    for j in range(len(abc)):
        if txt[i] == abc[j]:
            lst[j] += 1

max_val = 0
cnt = 0
for k in range(len(lst)):
    if max_val < lst[k]:
        max_val = lst[k]
        cnt = k

cnt1 = 0

for i in range(len(lst)):
    if max_val == lst[i]:
        cnt1 += 1
        if cnt1 == 2:
            print('?')
            break

else:
    print(abc[cnt])    