N = int(input())
li = [0]
temp = list(map(int, input().split()))

for i in temp :
    li.append(i)

dp = [0 for i in range(N + 1)]

dp[1] = li[1]

for i in range(2, N + 1) :
    for j in range(i, 0, -1) :
        dp[i] = max(dp[i], li[j] + dp[i - j])

print(dp[N])