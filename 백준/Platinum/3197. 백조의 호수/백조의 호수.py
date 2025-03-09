from collections import deque

# I think this problem is very very hard to people who first try to Platinum

qu = deque()
nqu = deque()
ml = deque()
nml = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS() :
    while qu :
        coo = qu.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y
            if nx < 0 or nx >= R or ny < 0 or ny >= C : continue 
            if vi[nx][ny] != -1 : continue
            if li[nx][ny] == 'X' : 
                nqu.appendleft([nx, ny])
                vi[nx][ny] = 0
                continue

            if li[nx][ny] == 'L' :
                if vi[nx][ny] == -1 : return 1

                else : continue

            vi[nx][ny] = 0
            qu.appendleft([nx, ny])

    return 0

def ml_BFS() :
    #print(ml)
    while ml :
        coo = ml.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(4) :
            nx = dx[i] + X
            ny = dy[i] + Y
            if nx < 0 or nx >= R or ny < 0 or ny >= C : continue 
            if xi[nx][ny] != -1 : continue
            if li[nx][ny] == 'X' :
                li[nx][ny] = '.'
                nml.append([nx, ny])
                xi[nx][ny] = 0
                continue
        
            xi[nx][ny] = 0
            ml.appendleft([nx, ny])
        

R, C = map(int, input().split())
xi = [[-1 for i in range(C)] for j in range(R)]
vi = [[-1 for i in range(C)] for j in range(R)]
li = []

for i in range(R) :
    li.append(list(input()))

ok = 0
day = 0

if R == 1 and C == 1 :
    print(0)

else :
    while ok == 0 :
        if nqu or nml :
            while nqu :
                qu.appendleft(nqu.pop())
            
            while nml :
                ml.appendleft(nml.pop())
        
        else :
            fi = 0
            for i in range(R) :
                for j in range(C) :
                    if li[i][j] == 'L' and fi == 0:
                        vi[i][j] = 0
                        qu.appendleft([i, j])
                        fi = 1
                        
                    if li[i][j] != 'X' :
                        xi[i][j] = 0
                        ml.appendleft([i, j])

        #print(day)
        ok = BFS()
        ml_BFS()
        day += 1


        '''for i in range(R) :
            for j in range(C) :
                print(vi[i][j], end = " ")
            print()'''

    print(day - 1)