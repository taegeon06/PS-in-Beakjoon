N, M = map(int, input().split())
li = list(map(int, input().split()))

pr = [0] * (N + 1)

ans = 0

for i in range(1, N + 1) :
    #if li[i - 1] % M == 0 :
        #ans += 1

    pr[i] = pr[i - 1] + li[i - 1]

    if pr[i] % M == 0 :
        ans += 1

mod = [0] * (N + 1)

for i in range(1, N + 1) :
    mod[i] = pr[i] % M

cnt = [0] * (M)

for i in range(1, N + 1) :
    cnt[mod[i]] += 1

for i in cnt :
    ans += i * (i - 1) // 2

print(ans)