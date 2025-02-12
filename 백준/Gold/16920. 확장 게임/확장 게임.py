from collections import deque

qu = deque()
tu = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS() :
    while qu :
        if tu :
            if li[tu[-1][0]][tu[-1][1]] != li[qu[-1][0]][qu[-1][1]] :
                coo = tu.pop()
            
            else :
                coo = qu.pop()

        else :
            coo = qu.pop()
        '''for i in range(N) :
            for j in range(M) :
                print(li[i][j], end = ' ')
            print()
        print('pass')'''
        #print(coo)
        X = coo[0]
        Y = coo[1]
        mo = coo[2]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y

            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if li[nx][ny] != '.' : continue

            if mo + 1 == S[int(li[X][Y]) - 1] : 
                qu.appendleft([nx, ny, 0])

            else :
                tu.appendleft([nx, ny, mo + 1])
            
            li[nx][ny] = li[X][Y]
        
def BFS_Mod() :
    while tu :
        coo = tu.pop()
        X = coo[0]
        Y = coo[1]
        mo = coo[2]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y

            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if li[nx][ny] != '.' : continue

            tu.appendleft([nx, ny, mo + 1])
            li[nx][ny] = li[X][Y]
        
N, M, P = map(int, input().split())
S = list(map(int, input().split()))
li = [list(input()) for i in range(N)]
ans = [0 for i in range(P)]

for k in range(P) :
    for i in range(N) :
        for j in range(M) :
            if li[i][j] == '.' or li[i][j] == '#' : continue
            if int(li[i][j]) != k + 1 : continue 
            qu.appendleft([i, j, 0])

BFS()
BFS_Mod()

for i in range(N) :
    for j in range(M) :
        if li[i][j] == '#' or li[i][j] == '.': continue

        ans[int(li[i][j]) - 1] += 1
    
for i in ans :
    print(i, end = " ")