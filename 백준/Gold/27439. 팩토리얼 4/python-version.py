def convolution_naive(a, b):
    n = len(a)
    m = len(b)
    ans = [0] * (n + m - 1)
    if n < m:
        for j in range(m):
            for i in range(n):
                ans[i + j] += a[i] * b[j]
    else:
        for i in range(n):
            for j in range(m):
                ans[i + j] += a[i] * b[j]
    return ans

def convolution_fft(a, b):
    n = len(a)
    m = len(b)
    z = 1 << (n + m - 1).bit_length()
    a += [0] * (z - n)
    b += [0] * (z - m)
    butterfly(a)
    butterfly(b)
    for i in range(z):
        a[i] *= b[i]
    butterfly_inv(a)
    a = a[:n + m - 1]
    iz = z.inv()
    for i in range(n + m - 1):
        a[i] *= iz
    return a



def convolution(a, b):
    n = len(a)
    m = len(b)
    if n == 0 or m == 0:
        return []
    if min(n, m) <= 60:
        return convolution_naive(a, b)
    return convolution_fft(a, b)

def Conv(n):
    s = str(n)
    ret = [int(s[i]) for i in range(len(s)-1, -1, -1)]
    return ret

def Mul(a, b):
    c = convolution(a, b)
    for i in range(len(c)):
        if c[i] > 9 and i + 1 == len(c):
            c.append(0)
        if c[i] > 9:
            c[i + 1] += c[i] // 10
            c[i] %= 10
    return c

def Sol(l, r):
    if l >= r:
        return Conv(l)
    mid = (l + r) // 2
    return Mul(Sol(l, mid), Sol(mid + 1, r))

n = int(input())
res = Sol(1, n)
for i in range(len(res)-1, -1, -1):
    print(res[i], end='')
print()
