N = int(input())
dp = [0] * (N + 4)

dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 1

for i in range(5, N + 1) :
    if dp[i - 1] % 2 == 0 :
        dp[i] = 1 + dp[i - 1]
    
    elif dp[i - 3] % 2 == 0 :
        dp[i] = 1 + dp[i - 3]
    
    elif dp[i - 4] % 2 == 0 :
        dp[i] = 1 + dp[i - 4]
    
    else :
        dp[i] = min(dp[i - 1], dp[i - 3], dp[i - 4]) + 1
    
if dp[N] % 2 == 0 :
    print('CY')

else :
    print('SK')