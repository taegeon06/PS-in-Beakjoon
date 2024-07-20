N = int(input())
M = int(input())
li = [int(input()) for i in range(M)]

dp = [0 for i in range(N + 2)]

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1

if N == M :
    print(ans)

else :

    cnt = 0
    for i in range(1, N + 1) :
        if not i in li :
            cnt += 1
            #print(cnt, i)
        
        else :
            if cnt != 0 :
                ans *= dp[cnt]
                cnt = 0

    if cnt > 0 :
        ans *= dp[cnt]

    print(ans)