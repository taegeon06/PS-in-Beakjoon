N, K = map(int, input().split())

li = [int(input()) for i in range(N)]
dp = [0 for i in range(K + 1)]

dp[0] = 1

for i in li :
    for j in range(i, K + 1) :
        dp[j] += dp[j - i]

print(dp[K])