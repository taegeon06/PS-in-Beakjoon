from collections import deque

qu = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS() :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = X + dx[i]
            ny = Y + dy[i]

            fk = False
            fd = False

            if nx < 0 or nx >= H or ny < 0 or ny >= W : continue
            if vi[nx][ny][len(ky)] != -1 : continue
            if li[nx][ny] == '*' : continue
            if li[nx][ny] == '$' : 
                fd = True

            if ord(li[nx][ny]) > 64 and ord(li[nx][ny]) < 91 :
                fn = False

                for j in ky :
                    if ord(li[nx][ny]) + 32 == ord(j) :
                        fn = True
                
                if not fn : continue

            if ord(li[nx][ny]) > 96 and ord(li[nx][ny]) < 123 :
                for j in ky :
                    if li[nx][ny] == j :
                        fk = True
                
                if not fk :
                    ky.append(li[nx][ny])
            
            if fd :
                vi[nx][ny][len(ky)] = 1
            
            else :
                vi[nx][ny][len(ky)] = 0

            qu.appendleft([nx, ny])

T = int(input())

for _ in range(T) :
    H, W = map(int, input().split())
    li = [list(input()) for i in range(H)]
    vi = [[[-1 for i in range(27)] for j in range(W)] for k in range(H)]
    cnt = [[0 for i in range(W)] for j in range(H)]
    ky = list(input())

    if ky[0] == '0' : ky.clear()

    cm = -1
    while cm != len(ky) :
        #print(cm, len(ky))
        #print('pass')
        cm = len(ky)

        for i in range(H) :
            for j in range(W) :
                if j == 0 or i == 0 or j == W - 1 or i == H - 1 :
                    if vi[i][j][len(ky)] != -1 : continue

                    if li[i][j] == '.' :
                        vi[i][j][len(ky)] = 0
                        qu.appendleft([i, j])
                        BFS()

                    elif li[i][j] == '$' :
                        vi[i][j][len(ky)] = 1
                        qu.appendleft([i, j])
                        BFS()

                    elif li[i][j] == '*' :
                        continue

                    elif ord(li[i][j]) > 64 and ord(li[i][j]) < 91 :
                        fn = False

                        for k in ky :
                            if ord(li[i][j]) + 32 == ord(k) :
                                fn = True

                        if not fn : continue

                        vi[i][j][len(ky)] = 0
                        qu.appendleft([i, j])
                        BFS()

                    elif ord(li[i][j]) > 96 and ord(li[i][j]) < 123 :
                        fn = False

                        for k in ky :
                            if li[i][j] == k :
                                fn = True

                        if not fn :
                            ky.append(li[i][j])

                        vi[i][j][len(ky)] = 0
                        qu.appendleft([i, j])
                        BFS()

    #print(vi)
    ans = 0
    for l in range(len(ky) + 1) :
        for i in range(H) :
            for j in range(W) :
                if vi[i][j][l] == 1 : 
                    if cnt[i][j] == 0 : 
                        cnt[i][j] = 1
                        ans += 1

    print(ans)