a, b = map(int, input().split())
ans = 1

while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break
    ans += 1

if b == a:
    print(ans)
else:
    print(-1)
