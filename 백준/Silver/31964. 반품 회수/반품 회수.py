N = int(input())
X = list(map(int, input().split()))
T_t = list(map(int, input().split()))
T = {}

for i in range(N) :
    T[X[i]] = T_t[i]

Ti = X[-1]

for i in range(X[-1], -1, -1) :
    if i in X :
        if Ti < T[i] :
            Ti += T[i] - Ti
    Ti += 1

print(Ti - 1)