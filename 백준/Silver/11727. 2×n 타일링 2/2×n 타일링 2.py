N = int(input())

dp = [[0 for i in range(N + 2)] for j in range(4)]

dp[1][1] = 1
dp[2][1] = 0
dp[3][1] = 0
dp[1][2] = 1
dp[2][2] = 1
dp[3][2] = 1
for i in range(3, N + 1) :
    dp[1][i] = dp[1][i - 1] + dp[2][i - 1] + dp[3][i - 1]
    dp[2][i] = dp[1][i - 2] + dp[2][i - 2] + dp[3][i - 2]
    dp[3][i] = dp[1][i - 2] + dp[2][i - 2] + dp[3][i - 2]

print((dp[1][N] + dp[2][N] + dp[3][N]) % 10007)