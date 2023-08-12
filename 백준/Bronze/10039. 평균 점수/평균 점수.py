ans = 0
for i in range(5):
    a = int(input())
    if a < 40:
        ans += 40
    else: ans += a
print(int(ans/5))