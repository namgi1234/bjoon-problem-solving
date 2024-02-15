N = int(input())

for _ in range(N):
    vps = input()
    count = 0
    for i in vps:
        if count < 0:
            break
        if i == "(":
            count += 1
        if i == ")":
            count -= 1
    if count == 0:
        print("YES")
    else:
        print("NO")