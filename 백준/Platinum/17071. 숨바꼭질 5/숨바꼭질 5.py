from collections import deque

#I referred blog.encrypted.gg and https://animoto1.tistory.com/

qu = deque()

dx = [-1, 1, 2]

def BFS() :
    while qu :
        coo = qu.pop()

        X = coo[0]
        ti = coo[1]

        for i in range(3) :
            if dx[i] == 2 :
                nx = X * dx[i]
            
            else :
                nx = X + dx[i]

            if nx < 0 or nx > 500000 : continue
            if vi[nx][(ti + 1) % 2] != -1 : continue
            
            vi[nx][(ti + 1) % 2] = vi[X][ti % 2] + 1
            qu.appendleft([nx, ti + 1])

N, K = map(int, input().split())
vi = [[-1, -1] for i in range(500001)]

vi[N][0] = 0
qu.appendleft([N, 0])

BFS()

ti = 0
ans = 1e9

temp = K

#print(vi)

'''for i in range(1, 6) :
    temp += i

print(temp)'''
#print(vi[temp])

while K <= 500000 :
    '''if K == temp :
        print(ti, vi[K])'''
        
    if ti == 0 :
        if vi[K][ti % 2] == ti :
            ans = min(vi[K][ti % 2], ans)
        
    else :
        if ti % 2 == vi[K][ti % 2] % 2 and vi[K][ti % 2] <= ti :
            ans = min(ti, ans)

    #print(ans)
    
    ti += 1
    K += ti


if ans == 1e9 :
    print(-1)
    
else :
    print(ans)