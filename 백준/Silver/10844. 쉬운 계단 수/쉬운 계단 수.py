N = int(input())

dp = [[0 for j in range(10)] for i in range(N + 1)]



for i in range(1, N + 1) :
    for j in range(0, 10) :
        if i == 1 :
            if j != 0 :
                dp[i][j] = 1
        
        else :
            if j == 0 :
                dp[i][j] += dp[i - 1][j + 1]
            
            elif j == 9 :
                dp[i][j] += dp[i - 1][j - 1]
            
            else :
                dp[i][j] += dp[i - 1][j + 1] + dp[i - 1][j - 1]

ans = 0

for i in range(10) :
    ans += dp[N][i]

print(ans % 1000000000)