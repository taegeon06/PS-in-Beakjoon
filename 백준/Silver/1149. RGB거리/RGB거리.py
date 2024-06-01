N = int(input())
dp = []
s = []
for i in range(N) :
    s.append(list(map(int, input().split())))
    dp.append([0, 0, 0])

dp[0] = s[0]

for i in range(1, N) :
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + s[i][0]
    dp[i][1] = min(dp[i - 1][2], dp[i - 1][0]) + s[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + s[i][2]

print(min(dp[N -1][0], dp[N - 1][1], dp[N - 1][2]))
    