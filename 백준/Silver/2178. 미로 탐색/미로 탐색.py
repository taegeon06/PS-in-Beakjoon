from collections import deque

N, M = map(int, input().split())

li = [list(input()) for i in range(N)]
vi = [[False] * M for i in range(N)] 
qu = deque()

dp = [[0] * M for i in range(N)]

#print(li)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 0

def BFS() :
    global cnt
    while qu :
        coo = qu.pop()
        cnt += 1
        X = coo[0]
        Y = coo[1]

        vicnt = 0
        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y
            if nx < 0 or nx >= N or ny < 0 or ny >= M : 
                vicnt += 1
                continue
            if vi[nx][ny] or li[nx][ny] != '1' : 
                vicnt += 1
                continue

            dp[nx][ny] = dp[X][Y] + 1
            vi[nx][ny] = True
            qu.appendleft([nx, ny])
        
        #if vicnt == 4 :
            #cnt -= 1

temp = []

for i in range(N) :
    for j in range(M) :
        if li[i][j] == '1' :
            temp.append([i, j])

for i, j in temp :
    if vi[i][j] :
        continue
    #print(i, j)
    qu.append([i, j])
    dp[i][j] += 1
    BFS()

print(dp[-1][-1])

#print(cnt)