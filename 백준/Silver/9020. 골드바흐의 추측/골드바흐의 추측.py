import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    a = [i for i in range(n)]
    s = []

    for i in range(2, n) :
        if a[i] == 0 : continue 
        s.append(a[i])

        for j in range(i + i, n, i) :
            a[j] = 0
    
    l, r = 0, n

    for i in range(len(s)) :
        for j in range(i, len(s)) :
            if s[i] + s[j] > n :
                f = 0
                break
        
            if s[i] + s[j] == n :
               if r - l > s[j] - s[i] :
                   l = s[i]
                   r = s[j]
                
    print(l, r)