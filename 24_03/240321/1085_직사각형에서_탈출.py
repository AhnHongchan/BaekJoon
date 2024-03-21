x,y,w,h = map(int, input().split())
ans = min(abs(x-0), abs(w-x), abs(y-0), abs(h-y))
print(ans)