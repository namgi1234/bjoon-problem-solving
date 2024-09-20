def count_ways(N):
    MOD = 10**9 + 7
    
    if N == 0:
        return 1
    elif N == 1:
        return 3
    
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 3
    
    for i in range(2, N + 1):
        dp[i] = (2 * dp[i - 1] + 2 * dp[i - 2]) % MOD
    
    return dp[N]

N = int(input())
print(count_ways(N))
