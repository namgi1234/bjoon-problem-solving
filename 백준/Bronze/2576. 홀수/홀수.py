import sys
arr = []
ans = 0

for _ in range(7):
    N = int(sys.stdin.readline())
    if N % 2 == 1:
        arr.append(N)
arr.sort()
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
