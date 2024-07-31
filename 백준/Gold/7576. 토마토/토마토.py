from collections import deque

M, N = map(int, input().split())

li = [list(map(int, input().split())) for i in range(N)]
vi = [[False] * M for i in range(N)]
qu = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
day = 0
mo = False


for i in range(N) :
    for j in range(M) :
        if li[i][j] == 1 :
            qu.append([i, j])
        
        elif li[i][j] == 0 :
            mo = True

def BFS() :
    cnt = 0
    tcnt = len(qu)
    global day

    while qu :
        coo = qu.pop()
        cnt += 1
        
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y

            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if vi[nx][ny] or li[nx][ny] == -1 : continue

            li[nx][ny] = 1
            vi[nx][ny] = True
            qu.appendleft([nx, ny])
        
        if cnt == tcnt :
            day += 1
            cnt = 0
            tcnt = len(qu)
        


if mo :
    BFS()
    fi = True

    for i in range(N) :
        if not fi :
            break

        for j in range(M) :
            if li[i][j] == 0 :
                fi = False
                break
            
    if fi :
        print(day - 1)

    else :
        print(-1)
        
else :
    print(0)