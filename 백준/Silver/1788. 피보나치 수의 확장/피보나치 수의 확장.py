N = int(input())

dp = [0 for i in range(abs(N) + 2)]

dp[0] = 0
dp[1] = 1

if N > 0 :
    print(1)

elif N == 0 :
    print(0)

else :
    if abs(N) % 2 == 0 :
        print(-1)
    
    else :
        print(1)
    
for i in range(2, abs(N) + 1) :
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000

print(dp[abs(N)])