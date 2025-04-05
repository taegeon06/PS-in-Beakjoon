n = int(input())

ai = list(map(int, input().split()))

cnt = 0

for i in range(n - 1) :
    if ai[i] == 0 :
        continue
    
    if ai[i] > ai[i + 1] :
        v = ai[i + 1]

        ai[i] -= v
        ai[i + 1] -= v
    
    else :
        v = ai[i]
        ai[i] -= v
        ai[i + 1] -= v

    cnt += 1

for i in range(n) :
    if ai[i] == 0 :
        continue
    
    ai[i] -= ai[i]
    cnt += 1

print(cnt)