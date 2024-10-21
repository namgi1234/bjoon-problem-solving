S = input()
key = "abcdefghijklmnopqrstuvwxyz"
arr = []
ans = 1

for i in S:
    arr.append(key.find(i))

for j in range(len(arr)):
    if j == len(arr) - 1 or arr[j] < arr[j+1]:
        continue
    else:
        ans += 1
print(ans)