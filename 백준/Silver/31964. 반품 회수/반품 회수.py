import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

Ti = X[-1]

for i in range(N - 1, -1, -1) :
    if Ti < T[i] :
        Ti += T[i] - Ti
    
    if i == 0 :
        Ti += X[i]

    else :
        Ti += X[i] - X[i - 1]
    #print("time : %d" %(X[i] - X[i - 1]))
    #print(X[i], X[i - 1], i)

print(Ti)