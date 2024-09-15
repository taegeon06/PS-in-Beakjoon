from collections import deque

qu = deque()
dx = [-1, 1, 0, 0, 0 ,0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def BFS() :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]
        Z = coo[2]

        for i in range(6) :
            nx = X + dx[i]
            ny = Y + dy[i]
            nz = Z + dz[i]

            if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C : continue
            if vi[nx][ny][nz][0] or li[nx][ny][nz] == '#' : continue
            if li[nx][ny][nz] == 'E' and vi[nx][ny][nz][0] :
                vi[nx][ny][nz][1] = min(vi[X][Y][Z][1] + 1, vi[nx][ny][nz][1])
                continue

            qu.appendleft([nx, ny, nz])
            vi[nx][ny][nz][0] = True
            vi[nx][ny][nz][1] = vi[X][Y][Z][1] + 1


while True :
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0 : break

    li = [[list(input()) for i in range(R + 1)] for j in range(L)]
    vi = [[[[False, 0] for l in range(C)] for i in range(R)] for j in range(L)]
    
    #print(vi)

    x1 = 0
    y1 = 0
    z1 = 0

    x2 = 0
    y2 = 0
    z2 = 0

    for i in range(L) :
        for j in range(R) :
            for k in range(C) :
                if li[i][j][k] == 'S' :
                    x1 = i
                    y1 = j
                    z1 = k

                    vi[i][j][k][0] = True
                    find = True
                    qu.appendleft([i, j, k])
                    BFS()
                
                if li[i][j][k] == 'E' :
                    x2 = i
                    y2 = j
                    z2 = k

    #print(vi)
    #print(x1, y1, z1)
    #print(x2, y2, z2)
    
    if vi[x2][y2][z2][1] == 0 :
        if x1 == x2 and y1 == y2 and z1 == z2 :
            print('Escaped in %d minute(s).' % (vi[x2][y2][z2][1]))
        
        else :
            print('Trapped!')
        
    else :
        print('Escaped in %d minute(s).' % (vi[x2][y2][z2][1]))
