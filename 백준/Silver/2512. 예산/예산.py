N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())

start = 0
last = arr[N-1]

ans = 0

while start <= last:
    middle = (start + last)//2
    total = 0
    for i in arr:
        total += min(i , middle)
    
    if total <= M :
        ans = middle
        start = middle + 1
    else :
        last = middle - 1

print(ans)