n = int(input())
ai = list(map(int, input().split()))

dp = [0 for i in range(n)]
dp1 = [0 for i in range(n)]

for i in range(n) :
    dp[i] = 1

    for j in range(n) :
        if ai[i] > ai[j] :
            dp[i] = max(dp[i], dp[j] + 1)
#print(dp)
for i in range(n - 1, -1, -1) :
    dp1[i] = 1

    for j in range(n - 1, -1, -1) :
        if ai[i] > ai[j] :
            dp1[i] = max(dp1[i], dp1[j] + 1)

ans = -1

for i in range(n) :
    ans = max(ans, dp[i] + dp1[i] - 1)

print(ans)