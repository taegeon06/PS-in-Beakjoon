T = int(input())

for i in range(T) :
    N = int(input())
    li = list(map(int, input().split()))
    M = int(input())

    dp = [0 for i in range(M + 1)]

    dp[0] = 1

    for j in range(N) :
        for k in range(li[j], M + 1, 1) :
            if j == 0 :
                dp[k] = dp[k - li[j]]
            
            else :
                dp[k] += dp[k - li[j]]
        
    #print(dp)
    print(dp[M])
