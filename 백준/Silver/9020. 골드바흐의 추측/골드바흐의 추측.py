def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())

for i in range(n):
    num = int(input())
    A = num // 2
    B = num // 2
    for j in range(num//2):
        if is_prime_number(A) and is_prime_number(B):
            print(A,B)
            break
        else:
            A -= 1
            B += 1