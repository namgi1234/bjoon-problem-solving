def matrix_multiply(a, b, mod):
    return (
        (a[0] * b[0] + a[1] * b[2]) % mod, (a[0] * b[1] + a[1] * b[3]) % mod,
        (a[2] * b[0] + a[3] * b[2]) % mod, (a[2] * b[1] + a[3] * b[3]) % mod
    )

def matrix_power(matrix, exp, mod):
    result = (1, 0, 0, 1)  # Identity matrix
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        exp //= 2
    return result

def fibonacci(n, mod):
    base_matrix = (1, 1, 1, 0)
    result_matrix = matrix_power(base_matrix, n - 1, mod)
    return result_matrix[0]

def pisano_period(M, P, N):
    n_modeM = N % M
    a, b = 1, 0
    candidate = [0] if N == 0 else [1] if N == 1 else []
    for i in range(2, P + 1):
        a, b = (a + b) % M, a
        if n_modeM == a:
            candidate.append(i)
    return candidate

N = int(input())

k = 3
M, P = 10**k, 15 * (10**(k - 1))
candidate = pisano_period(M, P, N)
M *= 10
for _ in range(3, 13):
    temp = [idx + m * P for idx in candidate for m in range(10) if fibonacci(idx + m * P, M) % M == N % M]
    candidate = temp[:]
    M, P = M * 10, P * 10
print(-1 if not candidate or N == 10**13 else min(candidate))
