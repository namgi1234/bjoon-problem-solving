N = int(input())

arr = set(map(int, input().split()))

M = int(input())

m = list(map(int, input().split()))

for i in range(M):
    print(int(m[i] in arr))