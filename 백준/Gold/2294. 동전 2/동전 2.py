N, K = map(int, input().split())
li = [int(input()) for i in range(N)]

li.sort()

dp = [1e9] * (K + 1)

dp[0] = 0

for i in range(1, K + 1) :
    for j in range(N) :
        if i < li[j] :
            break
        dp[i] = min(dp[i], dp[i - li[j]] + 1)


if dp[-1] == 1e9 :
    print(-1)

else :
    print(dp[-1])