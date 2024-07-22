N, M = map(int, input().split())

li = [list(input()) for i in range(N)]

dp = [[0 for i in range(M + 1)] for j in range(N + 1)]

ans = 0

for i in range(N) :
    for j in range(M) :
        if i == 0 or j == 0 :
            dp[i][j] = int(li[i][j])
            ans = max(dp[i][j], ans)

        else :
            #print(i, j)
            #print('pass')
            if int(li[i][j]) == 0 :
                dp[i][j] = 0
            
            else :
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1)
                ans = max(dp[i][j], ans)

#print(dp)
print(ans ** 2)