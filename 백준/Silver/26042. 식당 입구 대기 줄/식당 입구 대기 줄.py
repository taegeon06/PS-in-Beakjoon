from collections import deque
n = int(input())
qu = deque()

mx = 0
mn = 1e9

for i in range(n) :
    a = list(map(int, input().split()))

    if a[0] == 1 :
        qu.appendleft(a[1])
    
    else :
        qu.pop()
    
    if len(qu) > mx :
        mx = len(qu)
        mn = qu[0]
    
    elif len(qu) == mx :
        mn = min(qu[0], mn)
    
print(mx, mn)