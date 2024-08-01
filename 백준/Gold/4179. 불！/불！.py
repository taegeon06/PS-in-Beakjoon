from collections import deque

R, C = map(int, input().split())
li = [list(input()) for i in range(R)]
vi = [[False] * C for i in range(R)]
vij = [[False] * C for i in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
qu = deque()

se = False
ti = 0
ans = 1e9

def BFS() :
    ticnt = len(qu)
    cnt = 0
    global se, ti, ans

    while qu :
        #print(qu)
        #print(li)
        coo = qu.pop()
        cnt += 1
        X = coo[0]
        Y = coo[1]

        
        if li[X][Y] == 'J' :
            for i in range(4) :
                nx = dx[i] + X
                ny = dy[i] + Y

                if nx < 0 or nx >= R or ny < 0 or ny >= C :
                    ans = min(ans, ti)
                    se = True
                    continue
                
                if vij[nx][ny] or li[nx][ny] == '#' or li[nx][ny] == 'F' : continue

                vij[nx][ny] = True

                if vi[X][Y] :
                    li[X][Y] = 'F'
                else :
                    li[X][Y] = '.'
                li[nx][ny] = 'J'
                qu.appendleft([nx, ny])
        
        elif li[X][Y] == 'F' :
            for i in range(4) :
                nx = dx[i] + X
                ny = dy[i] + Y

                if nx < 0 or nx >= R or ny < 0 or ny >= C : continue

                if vi[nx][ny] or li[nx][ny] == '#' : continue

                if li[nx][ny] == 'J' :
                    for j in range(4) :
                        jnx = nx + dx[j]
                        jny = ny + dy[j]

                        if jnx < 0 or jnx >= R or jny < 0 or jny >= C :
                            se = True
                            ans = min(ans, ti)
                            continue
                        
                        if vij[jnx][jny] or li[jnx][jny] == '#' or li[jnx][jny] == 'F' : continue

                        vij[nx][ny] = True
                
                vi[nx][ny] = True
                
                if not vij[nx][ny] : li[nx][ny] = 'F'

                qu.appendleft([nx, ny])

        if cnt == ticnt :
            ti += 1
            cnt = 0
            ticnt = len(qu)
        
        #if se :
            #break


temp = []
fi = False

for i in range(R) :
    for j in range(C) :
        if li[i][j] == 'F' :
            fi = True
            qu.appendleft([i, j]) 
            vi[i][j] = True

for i in range(R) :
    for j in range(C) :
        if li[i][j] == 'J' :
            qu.appendleft([i, j])
            vij[i][j] = True

BFS()
#print(li)
if se :
    #if fi :
        #print(ti - 1)
        #print(ans + 1)
    
    #else :
        #print(ti)
       # print(ans + 1)
    print(ans + 1)

else :
    print('IMPOSSIBLE')