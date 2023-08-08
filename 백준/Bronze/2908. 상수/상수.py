a , b = map(str,input().split())

A = 100*int(a[2]) + 10*int(a[1]) + int(a[0])
B = 100*int(b[2]) + 10*int(b[1]) + int(b[0])

if int(A) > int(B):
    print(A)
else:
    print(B)