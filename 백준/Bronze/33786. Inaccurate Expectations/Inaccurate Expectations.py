n = int(input())

dp = [i for i in range(n + 1)]

for i in range(1, n + 1) :
    dp[i] = i + dp[i - 1] * i

#print(pref)
print(dp[n])