import math
from functools import reduce

def find_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def find_gcd(numbers):
    return reduce(math.gcd, numbers)

def find_common_divisors(numbers):
    gcd = find_gcd(numbers)
    return find_divisors(gcd)

def lcm(a, b):
    return a * b // math.gcd(a, b)

def find_lcm(numbers):
    return reduce(lcm, numbers)

d, m = map(int, input().split())

D = list(map(int, input().split()))
M = list(map(int, input().split()))

common_divisors = find_common_divisors(M)

common_lcm = find_lcm(D)

ans = sum(1 for i in common_divisors if i % common_lcm == 0)

print(ans)