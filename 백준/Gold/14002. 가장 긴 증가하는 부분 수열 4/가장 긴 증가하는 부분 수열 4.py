N = int(input())

li = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N) :
    for j in range(i) :
        if li[j] < li[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

se = max(dp)
ans = []
for i in range(N - 1, -1, -1) :
    if dp[i] == se :
        ans.append(li[i])
        se -= 1
ans.sort()

print(' '.join(map(str, ans)))