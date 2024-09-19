def factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

N, K = map(int, input().split())

print((factorial(N) // (factorial(K) * factorial(N-K)))%10007)