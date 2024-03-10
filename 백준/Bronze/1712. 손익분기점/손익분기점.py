import math

a, b, c = map(int,input().split())
try:
    if -a/(b-c) <= 0 or b-c ==0:
        print(-1)
    elif -a/(b-c)%1 == 0 :
        print(int(-a/(b-c))+1)
    else :
        print(math.ceil(-a/(b-c)))
except ZeroDivisionError:
    print(-1)