from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
qu = deque()
tcnt = 0

def BFS() :
    cnt = 0
    l = len(qu)

    global tcnt
    
    while qu :
        coo = qu.pop()
        cnt += 1
        X = coo[0]
        Y = coo[1]
        #print(X, Y)

        if li[X][Y] == '*' :
            for i in range(4) :
                nx = dx[i] + X
                ny = dy[i] + Y

                if nx < 0 or nx >= H or ny < 0 or ny >= W : continue
                if vi[nx][ny] or li[nx][ny] == '#' : continue

                if li[nx][ny] == '@' : 
                    vi[nx][ny] = True
                    qu.appendleft([nx, ny])

                if li[nx][ny] == '.' :
                    li[nx][ny] = '*'
                    vi[nx][ny] = True
                    qu.appendleft([nx, ny])
        
        elif li[X][Y] == '@' :
            for i in range(4) :
                nx = dx[i] + X
                ny = dy[i] + Y

                if nx < 0 or nx >= H or ny < 0 or ny >= W :
                    return True

                if pvi[nx][ny] or li[nx][ny] == '#' or li[nx][ny] == '*': continue
                
                pvi[nx][ny] = True
                qu.appendleft([nx, ny])

                if vi[X][Y] == True :
                    li[X][Y] = '*'
                    li[nx][ny] = '@'
                
                else :
                    li[X][Y] = '.'
                    li[nx][ny] = '@'

        if cnt == l :
            tcnt += 1
            cnt = 0
            l = len(qu)

    return False

for i in range(T) :
    W, H = map(int, input().split())
    li = []

    for j in range(H) :
        li.append(list(input()))
    
    vi = [[False] * W for j in range(H)]
    pvi = [[False] * W for j in range(H)]

    tcnt = 0
    qu.clear()

    for h in range(H) :
        for w in range(W) :
            if li[h][w] == '*' :
                qu.appendleft([h, w])
                vi[h][w] = True

    for h in range(H) :
        for w in range(W) :
            if li[h][w] == '@' :
                qu.appendleft([h, w])
                pvi[h][w] = True
    
    fi = BFS()

    if fi :
        print(tcnt + 1)
    
    else :
        print('IMPOSSIBLE')