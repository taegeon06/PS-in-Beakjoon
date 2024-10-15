from collections import deque

N, M = map(int, input().split())
li = []

for i in range(N) :
    li.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
qu = deque()
vi = [[[0, 0] for i in range(M)] for j in range(N)] 
# 벽 안부수고 이동/벽 부수고 이동/이동거리
#print(vi)
def BFS() :
    while qu :
        #print(qu)
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]
        D = coo[2]
        
        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y

            if nx < 0 or nx >= N or ny < 0 or ny >= M : 
                #print('pass')
                continue
            
            if nx == N - 1 and ny == M - 1 :
                if vi[nx][ny][D] != 0 :
                    #print('pass')
                    #print(vi[nx][ny][D], vi[X][Y][D] + 1)
                    vi[nx][ny][D] = min(vi[nx][ny][D], vi[X][Y][D] + 1)

            if li[nx][ny] == '1' and D == 0 :
                vi[nx][ny][1] = vi[X][Y][0] + 1
                qu.appendleft([nx, ny, 1])
            
            elif li[nx][ny] == '0' and  vi[nx][ny][D] == 0:
                vi[nx][ny][D] = vi[X][Y][D] + 1
                qu.appendleft([nx, ny, D])


qu.appendleft([0, 0, 0])
vi[0][0][0] = 1

BFS()

#print(vi)

ans = vi[N - 1][M - 1][0]
ans1 = vi[N - 1][M - 1][1]

if ans == 0 and ans1 == 0 :
    print(-1)

else :
    if ans != 0 and ans1 != 0 :
        print(min(ans, ans1))
    
    elif ans == 0 and ans1 != 0 :
        print(ans1)

    else :
        print(ans)
#print(ans, ans1)
