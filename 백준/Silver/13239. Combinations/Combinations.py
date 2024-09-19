import math

n = int(input())

for _ in range(n):
    N, K = map(int, input().split())
    print((math.factorial(N) // (math.factorial(K) * math.factorial(N-K)))%1000000007)