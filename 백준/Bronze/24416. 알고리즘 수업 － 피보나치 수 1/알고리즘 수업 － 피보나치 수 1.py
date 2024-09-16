import sys

n = int(sys.stdin.readline())

ans2 = 0

def fib(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

print(fib(n),n-2)