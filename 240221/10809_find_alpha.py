txt = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
blank = [-1] * 26
for i in range(26):
    for j in range(len(txt)):
        if alphabet[i] == txt[j]:
            if blank[i] == -1:
                blank[i] = j


print(*blank)