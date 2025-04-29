n = int(input())

cnt1 = 0
cnt2 = 0
ans = 1e9

idx = 1

while n >= idx * 5 :
    cnt1 = idx
    cnt2 = (n - idx * 5) // 2

    if cnt1 * 5 + cnt2 * 2 == n :
        ans = min(ans, cnt1 + cnt2)
    
    idx += 1

cnt2 = n // 2

if cnt2 * 2 == n :
    ans = min(ans, cnt2)

if ans == 1e9 :
    print(-1)

else :
    print(ans)