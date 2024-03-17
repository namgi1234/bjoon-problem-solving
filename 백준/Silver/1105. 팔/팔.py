l , r = input().split()
ans = 0
if len(l) != len(r):
    print(0)
elif l[0] != r[0]:
    print(0)
else :
    for i in range(len(l)):
        if l[i] != r[i]:
            break
        else:
            if l[i] == "8":
                ans += 1
    print(ans)
  