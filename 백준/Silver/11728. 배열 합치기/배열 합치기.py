n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
e = 0

while s != n and e != m :
    if a[s] < b[e] :
        print(a[s], end = ' ')
        s += 1
    
    elif a[s] > b[e] : 
        print(b[e], end = ' ')
        e += 1
    
    else :
        print(a[s], b[e], end = ' ')
        s += 1
        e += 1

if s < n :
    while s != n :
        print(a[s], end = ' ')
        s += 1
    
if e < m :
    while e != m :
        print(b[e], end = ' ')
        e += 1
