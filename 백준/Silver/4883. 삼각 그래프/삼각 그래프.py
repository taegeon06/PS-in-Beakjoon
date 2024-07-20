k = 0
while True :
    N = int(input())
    k += 1

    if N == 0 :
        break

    li = [list(map(int, input().split())) for i in range(N)]
    dp = [[0 for i in range(3)] for i in range(N)]

    dp[0][0] = li[0][0]
    dp[0][1] = li[0][1]
    dp[0][2] = li[0][2] + dp[0][1]

    for i in range(1, N) :
        if i == 1 :
            dp[i][0] = li[i][0] + dp[i - 1][1]
            dp[i][1] = li[i][1] + min(dp[i - 1][1], dp[i - 1][2], dp[i][0])
            dp[i][2] = li[i][2] + min(dp[i - 1][1], dp[i - 1][2], dp[i][1])

        else :
            dp[i][0] = li[i][0] + min(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = li[i][1] + min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0])
            dp[i][2] = li[i][2] + min(dp[i - 1][1], dp[i - 1][2], dp[i][1])

    print("%d. %d" %(k, dp[N - 1][1]))