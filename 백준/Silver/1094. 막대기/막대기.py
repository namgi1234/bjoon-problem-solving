n = int(input())
ans = 0
s = 64
while True:
    if n == 0:
        break
    else:
        if s > n:
            s = s//2
        else:
            ans += 1
            n -= s
print(ans)