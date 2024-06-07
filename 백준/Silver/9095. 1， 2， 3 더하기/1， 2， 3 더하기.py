T = int(input())

for i in range(T) :
    N = int(input())
    
    dp = []
    for i in range(N + 4) :
        dp.append(0)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if N < 4 :
        print(dp[N])
    else :
        for i in range(4, N + 1) :
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
        print(dp[N])