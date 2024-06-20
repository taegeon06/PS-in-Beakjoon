N = int(input())
li = [int(input()) for i in range(N)]
dp = [[0 for i in range(N + 2)] for j in range(3)]

li.append(0)
li.append(0)
li.append(0)


dp[0][0] = li[0]
dp[1][0] = li[0]
dp[0][1] = li[0] + li[1]
dp[0][2] = dp[1][1] + li[2]
dp[1][2] = max(dp[1][0], dp[0][0]) + li[2]
dp[2][0] = li[0]

for i in range(3, N) :
    dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + li[i]
    dp[1][i] = max(dp[1][i - 2], dp[0][i - 2], dp[2][i - 2]) + li[i]
    dp[2][i] = max(dp[0][i - 3], dp[1][i - 3], dp[2][i - 3]) + li[i]
    #print(max(dp[1][i - 2], dp[0][i - 2]), dp[1][i - 2], dp[0][i - 2])

ma = max(max(dp[0]), max(dp[1]), max(dp[2]))
dp.clear()
dp = [[0 for i in range(N + 3)] for j in range(3)]

dp[0][1] = li[1]
dp[1][1] = li[1]
dp[0][2] = li[1] + li[2]
dp[0][3] = dp[1][2] + li[3]
dp[1][3] = max(dp[1][1], dp[0][1]) + li[3]
dp[2][1] = li[1]

for i in range(4, N) :
    dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + li[i]
    dp[1][i] = max(dp[1][i - 2], dp[0][i - 2], dp[2][i - 2]) + li[i]
    dp[2][i] = max(dp[0][i - 3], dp[1][i - 3], dp[2][i - 3]) + li[i]
    #print(max(dp[1][i - 2], dp[0][i - 2]), dp[1][i - 2], dp[0][i - 2])

ma1 = max(max(dp[0]), max(dp[1]), max(dp[2]))

#print(dp)
print(max(ma, ma1))