e, s, m = map(int,input().split())

ans = 1

''' 
15*a + e = 28*b + s = 19*c + m
'''

while True:
    if (ans - e)%15 == 0 and (ans - s)%28 ==0  and (ans - m)%19 == 0 :
        break
    else :
        ans += 1
print(ans)