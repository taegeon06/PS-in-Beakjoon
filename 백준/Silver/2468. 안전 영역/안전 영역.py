from collections import deque

N = int(input())
li = []
vi = [[False] * N for i in range(N)]

for i in range(N) :
    li.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
qu = deque()

def BFS(l) :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = X + dx[i]
            ny = Y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
            if vi[nx][ny] or li[nx][ny] <= l : continue

            qu.appendleft([nx, ny])
            vi[nx][ny] = True


m = 0

for i in range(N) :
    m = max(max(li[i]), m)

cnt = 0

for i in range(0, m) :
    vi = [[False] * N for p in range(N)]
    
    tcnt = 0

    for j in range(N) :
        for k in range(N) :
            if vi[j][k] or li[j][k] <= i : continue

            #print(vi[j][k], j, k)
            #print('pass')

            tcnt += 1
            vi[j][k] = True
            qu.appendleft([j, k])

            BFS(i)
            #print(vi)
    #print('end')
    #print(tcnt)
    cnt = max(cnt, tcnt)

print(cnt)
