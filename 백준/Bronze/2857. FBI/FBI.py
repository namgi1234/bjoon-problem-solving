ans = []
count = 0
for i in range(1,6):
    code = input()
    if "FBI" in code:
        ans.append(i)
        count += 1
if count == 0:
    print("HE GOT AWAY!")
else :
    print(*ans)