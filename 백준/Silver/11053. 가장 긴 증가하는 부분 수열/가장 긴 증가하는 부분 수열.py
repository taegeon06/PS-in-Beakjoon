N = int(input())
li = list(map(int, input().split()))
dp = [0 for i in range(N)]

for i in range(N) :
    dp[i] = 1
    for j in range(i) :
        if li[i] > li[j] :
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))