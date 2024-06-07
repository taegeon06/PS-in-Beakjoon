import sys
input = sys.stdin.readline
N = int(input().rstrip())

dp1 = 1
dp2 = 2
dp3 = 0

for i in range(N - 2) :
    dp3 = (dp1 + dp2) % 15746
    dp1 = dp2
    dp2 = dp3

if N == 1 :
    print(1)
elif N == 2 :
    print(2)
else :
    print(dp3)