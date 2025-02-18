n = int(input())

while n > 0:
    if all(c in '47' for c in str(n)):
        print(n)
        break
    n -= 1

if n == 0:
    print(-1)