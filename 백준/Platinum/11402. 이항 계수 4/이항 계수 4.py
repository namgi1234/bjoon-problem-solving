import math
n,m,d=map(int,input().split())
x=1
while n*m*x:
    x=x*math.comb(n%d,m%d)%d
    n//=d;m//=d
print(x)