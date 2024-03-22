import sys
N = int(sys.stdin.readline())
q = []
for _ in range(N):
    a = sys.stdin.readline().rstrip()
    if a in q:
        pass
    else:
        q.append(a)

q.sort()
q.sort(key = len)
print(*q, sep="\n")