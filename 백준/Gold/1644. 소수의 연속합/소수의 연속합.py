n = int(input())
a = [1 for i in range(n + 1)]
v = []

for i in range(2, n + 1) :
    if a[i] != 0 :
        v.append(i)
    
    for j in range(i + i, n + 1, i) :
        a[j] = 0
    
#print(v)

ans = 0
sum = 0
s = 0
e = 0

while 1 :
    if sum >= n :
        sum -= v[s]
        s += 1

    elif e == len(v) : break

    else :
        sum += v[e]
        e += 1
    
    if sum == n :
        ans += 1
    
print(ans)