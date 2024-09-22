import math
import sys

n,k = map(int, sys.stdin.readline().split())

print(math.comb(n+k-1,k-1)%1000000000)