import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int,input().split()))

temp = [0]

for i in range(n):
    temp.append(temp[i] + arr[i])

for _ in range(m):
    i , j = map(int, input().split())
    print(temp[j]-temp[i-1])