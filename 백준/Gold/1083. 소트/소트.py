n=int(input())
a=list(map(int, input().split()))
k=int(input())
i=0
while k>0 and i<n:
    m=a.index(max(a[i:i+k+1]))
    if m!=i: 
        a[m],a[m-1]=a[m-1],a[m];k-=1 
    else:i+=1 
print(*a)