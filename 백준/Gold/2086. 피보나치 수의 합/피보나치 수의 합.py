MOD = 10**9
vii = list[list[int]]
vi = list[int]

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

def matrix_multiply(a: vii, b: vii) -> vii:
    sz = len(a)
    ret = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            for k in range(sz):
                ret[i][j] += a[i][k] * b[k][j]
            ret[i][j] %= MOD
    return ret

def matrix_power(a: vii, b: int) -> vii:
    sz = len(a)
    ret = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        ret[i][i] = 1
    while b:
        if b % 2:
            ret = matrix_multiply(ret, a)
        b //= 2
        a = matrix_multiply(a, a)
    return ret

n, m = map(int, input().split())
A = [[1, 1], [1, 0]]
a = matrix_power(A, n + 1)
b = matrix_power(A, m + 2)
ans = (b[0][1] - a[0][1] + MOD) % MOD
print(ans)
