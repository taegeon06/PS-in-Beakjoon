N = int(input())

dp = [0 for i in range(N + 2)]

dp[1] = 1
dp[2] = 2

for k in range(3, N + 1) :
    dp[k] = dp[k - 1] + dp[k - 2]

print(dp[N] % 10007)