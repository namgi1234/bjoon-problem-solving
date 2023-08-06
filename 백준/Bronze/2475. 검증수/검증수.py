a = list(map(int,input().split()))

def func():
    return (a[0]**2 + a[1] ** 2 + a[2]**2 + a[3]**2 +a[4]**2)%10

print(func())