import sys
import math

n,k  = map(int,sys.stdin.readline().split())

if n == 1 or n==2:
    print(1)
else:
    print(int(math.factorial(n-1)/(math.factorial(k-1)*math.factorial(n-k))))