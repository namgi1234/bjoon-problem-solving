t = int(input())

for _ in range(1,t+1):
    dp = [0,1,2,4,7]
    n = int(input())
    if n <= 4:
        print(dp[n])
    else:
        for i in range(5,n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
        print(dp[n])
