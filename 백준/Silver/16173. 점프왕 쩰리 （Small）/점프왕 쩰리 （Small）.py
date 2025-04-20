n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
vi = [[0 for i in range(n)] for j in range(n)]

dx = [1, 0]
dy = [0, 1]

st = []

def dfs() :
    while st :
        coo = st.pop()
        X = coo[0]
        Y = coo[1]

        for i in range(2) :
            nx = X + dx[i] * a[X][Y]
            ny = Y + dy[i] * a[X][Y]

            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if vi[nx][ny] == 1 : continue
            if a[nx][ny] == -1 :
                return 'HaruHaru'
            
            st.append([nx, ny])
            vi[nx][ny] = 1
        
    return 'Hing'

st.append([0, 0])
print(dfs())