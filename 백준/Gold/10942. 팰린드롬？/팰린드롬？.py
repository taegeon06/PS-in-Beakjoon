import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for i in range(N)]

for i in range(N) :
    for j in range(N - i) :
        s = j
        e = j + i
        if s == e :
            dp[s][e] = 1
        
        elif li[s] == li[e] :
            if s + 1 == e :
                dp[s][e] = 1
            
            elif dp[s + 1][e - 1] == 1 :
                dp[s][e] = 1

#print(dp)
for i in range(M) :
    S, E = map(int, input().split())

    print(dp[S - 1][E - 1])