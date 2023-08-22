import sys
input = lambda : sys.stdin.readline()

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N-1):
    for j in range(M):
        min_value = min(arr[i][:j] + arr[i][j+1:])
        arr[i+1][j] += min_value
      
print(min(arr[-1]))