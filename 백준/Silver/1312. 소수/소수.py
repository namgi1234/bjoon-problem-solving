A,B,N = map(int, input().split())

result = 0

for _ in range(N) :
    A = (A%B)*10
    result = A//B

print(result)