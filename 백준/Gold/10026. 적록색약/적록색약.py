from collections import deque

N = int(input())

li = [list(input()) for i in range(N)]
vi = [[False] * N for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
qu = deque()

def nomal_BFS() :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y

            if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
            if vi[nx][ny] or li[nx][ny] != li[X][Y] : continue
            
            vi[nx][ny] = True
            qu.appendleft([nx, ny])

def unique_BFS() :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y

            if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
            if vi[nx][ny] : continue
            if li[X][Y] != li[nx][ny] :
                if not ((li[X][Y] == 'R' and li[nx][ny] == 'G') or (li[X][Y] == 'G' and li[nx][ny] == 'R')) :
                    continue
            
            vi[nx][ny] = True
            qu.appendleft([nx, ny])

ncnt = 0
for i in range(N) :
    for j in range(N) :
        if vi[i][j] :
            continue
        ncnt += 1
        vi[i][j] = True
        qu.appendleft([i, j])
        nomal_BFS()

vi = [[False] * N for i in range(N)]
qu.clear()

ucnt = 0
for i in range(N) :
    for j in range(N) :
        if vi[i][j] :
            continue

        ucnt += 1
        vi[i][j] = True
        qu.appendleft([i, j])
        unique_BFS()
    
print(ncnt, ucnt, end = " ")