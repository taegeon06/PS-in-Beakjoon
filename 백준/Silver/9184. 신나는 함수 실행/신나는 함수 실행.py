a, b, c = map(int, input().split())

while True :
    if a == -1 and b == -1 and c == -1 :
        break

    if a <= 0 or b <= 0 or c <= 0 :
        print('w(%d, %d, %d) = %d' %(a, b, c, 1))

    else :
        dp = [[[0 for i in range(51)] for j in range(51)] for k in range(51)]

        for i in range(21) :
            for j in range(21) :
                for k in range(21) :
                    if i <= 0 or j <= 0 or k <= 0 :
                        dp[i][j][k] = 1

                    elif i > 20 or j > 20 or k > 20 :
                        dp[i][j][k] = dp[20][20][20]

                    elif i < j and j < k :
                        dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]

                    else :
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

        for i in range(a + 1) :
            for j in range(b + 1) :
                for k in range(c + 1) :
                    if i <= 0 or j <= 0 or k <= 0 :
                        dp[i][j][k] = 1

                    elif i > 20 or j > 20 or k > 20 :
                        dp[i][j][k] = dp[20][20][20]

                    elif i < j and j < k :
                        dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]

                    else :
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

        print('w(%d, %d, %d) = %d' %(a, b, c, dp[a][b][c]))

    a, b, c = map(int, input().split())
