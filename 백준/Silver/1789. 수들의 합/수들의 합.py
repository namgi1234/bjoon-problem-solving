n = int(input())
total = 0
ans = 1

while total <= n:
    total += ans
    ans += 1

print(ans-2)