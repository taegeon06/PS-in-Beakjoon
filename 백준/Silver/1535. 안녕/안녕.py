# i referred to https://lrl.kr/cW0vx

n = int(input())

a = [[0, 0] for i in range(n)]
dp = [[0 for j in range(100)] for i in range(n)]
l = list(map(int, input().split()))
j = list(map(int, input().split()))

for i in range(n) :
    a[i][0] = l[i]
    a[i][1] = j[i]

for i in range(100) :
    if a[0][0] <= i :
        dp[0][i] = a[0][1]
    
for i in range(1, n) :
    for j in range(1, 100) :
        if a[i][0] <= j :
            dp[i][j] = max(dp[i - 1][j - a[i][0]] + a[i][1], dp[i - 1][j])
        
        else :
            dp[i][j] = dp[i - 1][j]
        
print(max(dp[n - 1]))