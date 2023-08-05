n, k = map(int, input().split())

userInput = list(map(int,input().split()))

arr = sorted(userInput)

print(arr[k-1])