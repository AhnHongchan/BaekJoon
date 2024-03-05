N = int(input())
lst = list(map(int, input().split()))
a = max(lst)

for i in range(N):
    lst[i]= lst[i] / a * 100

avg = sum(lst)/N

print(avg)