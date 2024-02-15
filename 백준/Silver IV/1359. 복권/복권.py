from math import comb

n , m , k = map(int,input().split())

ans = 0
for i in range(k,m+1):
    ans += comb(m,i)*comb(n-m,m-i)/comb(n,m)

print(ans)