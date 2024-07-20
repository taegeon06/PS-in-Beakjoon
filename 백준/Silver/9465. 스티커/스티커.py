T = int(input())

for i in range(T) :
    N = int(input())
    li = [list(map(int, input().split())) for j in range(2)]
    dp = [[0 for j in range(N + 1)] for k in range(2)]

    if N > 1 :
        dp[0][0] = li[0][0]
        dp[1][0] = li[1][0]

        dp[0][1] = dp[0][0] + li[1][1]
        dp[1][1] = dp[1][0] + li[0][1]
        
        for j in range(2, N) :
            if j % 2 == 0 :
                dp[0][j] = li[0][j] + max(dp[0][j - 1], dp[1][j - 2])
                dp[1][j] = li[1][j] + max(dp[1][j - 1], dp[0][j - 2])

            else :
                dp[0][j] = li[1][j] + max(dp[0][j - 1], dp[1][j - 2])
                dp[1][j] = li[0][j] + max(dp[1][j - 1], dp[0][j - 2])
        #print(dp[0])
        #print(dp[1])
        print(max(dp[0][N - 1], dp[1][N - 1]))
    else :
        print(max(li[0][0], li[1][0]))