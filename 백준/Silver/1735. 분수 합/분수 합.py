import math

a,b = map(int,input().split())
c,d = map(int,input().split())

A = c*b + a*d
B = b*d

print(A // math.gcd(A,B), B // math.gcd(A,B))