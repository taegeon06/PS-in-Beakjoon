N = int(input())
dp = []
s = []

dp.append([0, 0, 0])
s.append(0)
for i in range(N) :
    dp.append([0, 0, 0])
    s.append(int(input()))
dp.append([0, 0, 0])
s.append(0)

dp[1][1] = s[1]
dp[2][1] = s[2]
dp[2][2] = s[1] + s[2]

for i in range(3, N + 1) :
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + s[i]
    dp[i][2] = dp[i - 1][1] + s[i]

print(max(dp[N][1], dp[N][2]))