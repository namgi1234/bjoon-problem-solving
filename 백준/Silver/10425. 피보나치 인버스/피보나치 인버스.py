N = int(input())

def find_largest_i(n):
    fib_sequence = [0, 1]
    i = 2

    while True:
        fib_i = fib_sequence[i-1] + fib_sequence[i-2]
        if fib_i <= n:
            fib_sequence.append(fib_i)
            i += 1
        else:
            break

    return i - 1

for _ in range(N):
    a = int(input())
    print(find_largest_i(a))