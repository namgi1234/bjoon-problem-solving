def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_smallest_palindrome_prime(N):
    num = N
    while True:
        if is_prime(num) and is_palindrome(num):
            return num
        num += 1

N = int(input())
result = find_smallest_palindrome_prime(N)
print(result)