from collections import deque

F, S, G, U, D = map(int, input().split())

li = [[False, 0] for i in range(F + 1)] 

#print(li)

qu = deque()

dx = [D, U]
dx[0] *= -1

def BFS() :
    while qu :
        X = qu.pop()

        for i in range(2) :
            nx = dx[i] + X

            if nx < 1 or nx >= F + 1: continue
            if li[nx][0] : 
                if nx == G :
                    li[nx][1] = min(li[nx][1], li[X][1] + 1)
                continue

            qu.appendleft(nx)

            #print('pass')
            #li[nx][1] = li[X][1] + 1

            li[nx][0] = True
            li[nx][1] = li[X][1] + 1

qu.appendleft(S)
li[S][0] = True

BFS()

#print(li)

if li[G][1] == 0 :
    if S == G :
        print(0)
    
    else :
        print('use the stairs')

else :
    print(li[G][1])

#print(li)
