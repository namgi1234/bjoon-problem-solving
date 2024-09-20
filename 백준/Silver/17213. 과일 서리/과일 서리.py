import math

n = int(input())
m = int(input())

k = m-n

print(math.factorial(n+k-1)//(math.factorial(k)*math.factorial(n-1)))