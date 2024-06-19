N = int(input())
li = list(map(int, input().split()))

dp = li.copy()

for i in range(N) :
    
    for j in range(0, i) :
        if li[i] > li[j] :
            dp[i] = max(dp[i], dp[j] + li[i])
        
        #print('i = %d, dp[i] = %d' %(i, dp[i]))
#print(li)
#print(dp)
print(max(dp))