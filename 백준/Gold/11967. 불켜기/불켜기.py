from collections import deque

qu = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS() :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]

        while li[X][Y] :
            tm = li[X][Y].pop()
            rx = tm[0]
            ry = tm[1]
            #print('pass')
            #print(X, Y, rx, ry)

            if vi[rx][ry] : continue
            if CHK(rx, ry) :
                vi[rx][ry] = 1
                qu.appendleft([rx, ry])
            
            fr[rx][ry] = 1
        
        for i in range(4) :
            nx = X + dx[i]
            ny = Y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
            if vi[nx][ny] == 1 or fr[nx][ny] == 0 : continue

            vi[nx][ny] = 1
            qu.appendleft([nx, ny])

def CHK(X, Y) :
    for i in range(4) :
        nx = dx[i] + X
        ny = dy[i] + Y
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
        if vi[nx][ny] == 1 : return True
    
    return False

N, M = map(int, input().split())
li = [[deque() for i in range(N)] for j in range(N)]
vi = [[0 for i in range(N)] for j in range(N)]
fr = [[0 for i in range(N)] for j in range(N)]

for i in range(M) :
    x, y, a, b = map(int, input().split())
    li[x - 1][y - 1].append([a - 1, b - 1])

vi[0][0] = 1
fr[0][0] = 1
qu.appendleft([0, 0])

BFS()

ans = 0

for i in range(N) :
    for j in range(N) :
        ans += fr[i][j]

print(ans)