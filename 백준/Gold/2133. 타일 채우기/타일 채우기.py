N = int(input())

dp = [0] * (N + 4)

dp[0] = 1
dp[2] = 3
dp[4] = 11

for i in range(6, N + 1) :
    if i % 2 == 0 :
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(4, i, 2) :
            #print(dp[i - j], dp[j], i - j, j)
            dp[i] += dp[i - j] * 2 
            
#print(dp)
print(dp[N])