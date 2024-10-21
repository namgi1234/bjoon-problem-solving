N = int(input())
arr = list(map(int, input().split()))

count = 1

for i in range(N):
    if i == N-1 or arr[i] > arr[i+1]:
        continue
    else :
        count += 1

print(count)