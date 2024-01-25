def sieve_of_eratosthenes_optimized(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, limit+1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def nth_prime_optimized(n):
    if n < 1:
        return None

    limit = 500000
    while True:
        primes = sieve_of_eratosthenes_optimized(limit)
        if len(primes) >= n:
            return primes[n - 1]

        limit *= 2

# 사용자로부터 n을 입력 받습니다.
n = int(input())

# n번째 소수를 출력합니다.
print(nth_prime_optimized(n))