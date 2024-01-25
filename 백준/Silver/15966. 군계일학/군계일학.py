n = int(input())
num_arr = list(map(int, input().split()))

long_arr = [1] * n
num_idx_map = {num_arr[0]: 0}
max_long = 1

for i in range(1, n):
    if num_arr[i] - 1 in num_idx_map:
        long_arr[i] = long_arr[num_idx_map[num_arr[i] - 1]] + 1
    else:
        long_arr[i] = 1

    max_long = max(max_long, long_arr[i])
    num_idx_map[num_arr[i]] = i

print(max_long)
