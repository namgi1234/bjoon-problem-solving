n = int(input())
m = int(input())

s = [0] * (n + 1)
for i in range(2, n + 1):
    if s[i] == 0:
        s[i:n+1:i] = [max(s[t], i) for t in range(i, n + 1, i) if t % i == 0]

ans = sum(1 for i in s if i <= m) - 1
print(ans)
