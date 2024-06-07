N = int(input())

dp = []

for i in range(N + 1) :
    dp.append([0, 0, 0])
dp.append([0, 0, 0])
dp[1][1] = 1
dp[1][2] = 0
dp[2][1] = 1
dp[2][2] = 1

for i in range(3, N + 1) :
    dp[i][1] = dp[i - 1][1] + dp[i - 1][2]
    dp[i][2] = dp[i - 2][1] + dp[i - 2][2]

print((dp[N][1] + dp[N][2]) % 10007)