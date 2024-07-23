li = input()

dp = [0] * (len(li) + 1)

dp[0] = 1

for i in range(0, len(li)) :
    if i == 0 :
        if int(li[0]) == 0 :
            break

        else :
            dp[i + 1] = 1
        
    else :
        temp = int(li[i - 1 : i + 1])
        if int(li[i]) > 0 :
            dp[i + 1] += dp[i]
        
        if 10 <= temp <= 26 :
            dp[i + 1] += dp[i - 1]
    
print(dp[len(li)] % 1000000)