n, m = map(int, input().split())
A = list(map(int, input().split()))

sex = 0
count = 0

# 뒤에서부터 탐색
for i in range(n-1, -1, -1):
    sex += A[i]
    if sex >= m:
        print(i + 1)  # 문제에서 1-based 인덱스를 요구하므로 +1
        break
    count += 1

if sex < m:
    print(-1)
