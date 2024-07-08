N = int(input())

li = []

for i in range(N) :
    li.append(list(map(int, input().split())))

dp = [0 for i in range(N + 1)]

pr = 0

for i in range(N) :
    pr = max(pr, dp[i])

    if i + li[i][0] <= N :
        dp[i + li[i][0]] = max(pr + li[i][1], dp[i + li[i][0]])

print(max(dp))