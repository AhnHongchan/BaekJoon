import sys
input = sys.stdin.readline
string = input().rstrip()

cnt = 0
dic = {}
for i in range(len(string)):
    for j in range(len(string)):
        if 0 <= i+j < len(string):
            if string[i:i+j+1] in dic:
                continue
            else:
                dic[string[i:i+j+1]] = 1

print(len(dic))