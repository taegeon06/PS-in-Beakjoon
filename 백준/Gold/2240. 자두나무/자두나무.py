T, W = map(int, input().split())
dp = [[0 for i in range(W + 1)] for j in range(T + 1)]

for i in range(1, T + 1) :
    wi = int(input())
    if wi == 1 :
        dp[i][0] = dp[i - 1][0] + 1
    
    else :
        dp[i][0] = dp[i - 1][0]

    
    for j in range(1, W + 1) :
        if j % 2 == 0 and wi == 1 :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        
        elif j % 2 == 1 and wi == 2 :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])


print(max(dp[-1]))