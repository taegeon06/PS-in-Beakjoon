from collections import deque

n = int(input())

qu = deque()
p = [0 for i in range(n + 1)]
nod = [[] for i in range(n + 1)]

for i in range(n - 1) :
    a, b = map(int, input().split())

    nod[a].append(b)
    nod[b].append(a)

qu.appendleft(1)

while qu :
    cur = qu.pop()

    for nx in nod[cur] :
        if p[cur] == nx : continue
        qu.appendleft(nx)
        p[nx] = cur
    
for i in range(2, n + 1) :
    print(p[i])