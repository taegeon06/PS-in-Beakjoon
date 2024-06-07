import math

T = int(input())

for i in range(T) :
    N = int(input())

    if N % 2 == 0 :
        temp = N // 2
    
    else :
        temp = math.trunc(N) // 2 + 1

    dp = [[0 for i in range(N + 4)] for j in range(2)]
    dp[0][1] = 1
    dp[1][1] = 1
    dp[0][2] = 1
    dp[1][2] = 2
    dp[0][3] = 2
    dp[1][3] = 3
    dp[0][4] = 4
    dp[1][4] = 5

    for i in range(5, temp + 1) :
        dp[0][i] = dp[1][i - 1] + dp[1][i - 3]
        dp[1][i] = dp[0][i] + dp[0][i - 2] 
        #print("dp[%d][%d] = %d" % (0, i, dp[0][i]))
        #print("dp[%d][%d] = %d" % (1, i, dp[1][i]))

    if N < 9 :
        if N % 2 == 0 :
            print(dp[1][temp])
    
        else :
            print(dp[0][temp])

    else :
        ans = 0
        for i in range(N, -1, -1) :
            #print("dp[%d][%d] = %d" % (0, i, dp[0][i]))
            #print("dp[%d][%d] = %d" % (1, i, dp[1][i]))
            if dp[1][i] != 0 :
                ans = i
                break

            if dp[0][i] != 0 :
                ans = i
                break
        #print("ans = %d" % (ans))
        if N % 2 == 0 :
            print(dp[1][ans])
    
        else :
            print(dp[0][ans])