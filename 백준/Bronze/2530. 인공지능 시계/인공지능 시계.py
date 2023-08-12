import sys
a,b,c = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

h = n//3600
m = (n%3600)//60
s = ((n%3600)%60)

ps = (s+c)%60
pm = (b+m+((s+c)//60))%60
ph = (a+h+((b+m+((s+c)//60))//60))%24

print(ph,pm,ps)