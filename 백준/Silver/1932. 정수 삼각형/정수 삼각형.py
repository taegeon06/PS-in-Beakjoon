N = int(input())

li = [list(map(int, input().split())) for i in range(N)]

dp = [[0] * N for i in range(N)]
dp[0][0] = li[0][0]

for i in range(1, N) :
    for j in range(0, i + 1) :
        if j == 0 :
            dp[i][j] = dp[i - 1][j] + li[i][j]

        elif j == i :
            dp[i][j] = dp[i - 1][j - 1] + li[i][j]
            
        else :
            dp[i][j] = max(dp[i - 1][j - 1] + li[i][j], dp[i - 1][j] + li[i][j]) 

print(max(dp[N - 1]))