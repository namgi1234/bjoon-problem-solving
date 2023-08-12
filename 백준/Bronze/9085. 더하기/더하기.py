N = int(input())

for i in range(N):
    a = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))