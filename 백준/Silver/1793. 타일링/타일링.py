while (True):
    try:
        n = int(input())

        dp = [0]*251

        dp[0] = 1
        dp[1] = 1

        if n > 1:
            for i in range(2,n+1):
                dp[i] = dp[i-1]+dp[i-2]*2
            print(dp[n])
        else :
            print(1)
        
    except:
        break