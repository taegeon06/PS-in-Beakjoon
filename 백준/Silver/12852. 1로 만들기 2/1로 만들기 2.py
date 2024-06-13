N = int(input())

dp = [0 for i in range(N + 1)]
dp.append(0)
dp.append(0)

dp[1] = [1, 1]
dp[2] = [1, 1]
dp[3] = [1, 1]

for i in range(4, N + 1) :
    c1 = 1e9
    c2 = 1e9
    c3 = dp[i - 1][0] + 1

    if i % 3 == 0 :
        c1 = dp[i // 3][0] + 1
    
    if i % 2 == 0 :
        c2 = dp[i // 2][0] + 1

    temp = min(c1, c2, c3)

    if temp == c1 :
        dp[i] = [c1, i // 3]
    
    elif temp == c2 :
        dp[i] = [c2, i // 2]
    
    else :
        dp[i] = [c3, i - 1]
    


if N == 1 :
    print(0)
    print(1)

else :
    print(dp[N][0])
    print(N, end = " ")

    temp = dp[N][1]
    while temp != 1 :
        print(temp, end = " ")
        temp = dp[temp][1]
    print(1)