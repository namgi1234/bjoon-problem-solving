ans = 0
while True:
    try:
        string = input()
        ans += 1
    except EOFError:
        break
print(ans)