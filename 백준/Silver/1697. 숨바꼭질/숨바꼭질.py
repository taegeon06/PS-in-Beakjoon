from collections import deque

N, K = map(int, input().split())

l = max(N, K)
dx = [1, -1, 2]
vi = [False] * (10000000)
fi = False
qu = deque()
ti = 0
ans = 0

def BFS() :
    lqu = len(qu)
    cnt = 0
    global ti, ans

    while qu :
        X = qu.pop()
        cnt += 1

        if X == K :
            ans = ti
            break
        
        for i in range(3) :
            if dx[i] == 2 :
                nx = X * dx[i]
            
            else :
                nx = X + dx[i]

            #print(nx)

            if nx < 0 or nx >= len(vi) : continue
            if vi[nx] : continue

            qu.appendleft(nx)
            vi[nx] = True
        
        if cnt == lqu :
            #print(qu)
            cnt = 0
            lqu = len(qu)
            ti += 1

qu.appendleft(N)
vi[N] = True
BFS()

#print(fi)
print(ans)