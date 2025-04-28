n = int(input())
a = dict()

for i in range(n) :
    s, x = input().split()

    x = int(x)

    if not a.get(s) :
        a[s] = x
    
    else : a[s] += x

ans = 'NO'

for i in a.values() :
    if i == 5 :
        ans = 'YES'
    
print(ans)