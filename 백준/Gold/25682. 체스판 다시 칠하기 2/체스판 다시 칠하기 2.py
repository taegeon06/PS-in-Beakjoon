import copy, sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

li = []

for i in range(N) :
    li.append(list(input()))

#pr = [[0] * (M + 1) for i in range(N + 1)]

liB = copy.deepcopy(li)
liW = copy.deepcopy(li)
cnB = [[0] * (M + 1) for i in range(N + 1)]
cnW = [[0] * (M + 1) for i in range(N + 1)]

if li[0][0] == 'B' : 
    for i in range(N) :
        for j in range(M) :
            if i == 0 and j == 0 :
                continue

            if j != 0 :
                if liB[i][j] == liB[i][j - 1] :
                    if liB[i][j] == 'B' :
                        liB[i][j] = 'W'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 
                    
                    else :
                        liB[i][j] = 'B'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

                else :
                    cnB[i + 1][j + 1] = cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

            else :
                if liB[i][j] == liB[i - 1][j] :
                    if liB[i][j] == 'B' :
                        liB[i][j] = 'W'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 
                    
                    else :
                        liB[i][j] = 'B'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

                else :
                    cnB[i + 1][j + 1] = cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

else :
    liB[0][0] = 'B'
    cnB[1][1] = 1

    for i in range(N) :
        for j in range(M) :
            if i == 0 and j == 0 :
                continue

            if j != 0 :
                if liB[i][j] == liB[i][j - 1] :
                    if liB[i][j] == 'B' :
                        liB[i][j] = 'W'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 
                    
                    else :
                        liB[i][j] = 'B'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

                else :
                    cnB[i + 1][j + 1] = cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

            else :
                if liB[i][j] == liB[i - 1][j] :
                    if liB[i][j] == 'B' :
                        liB[i][j] = 'W'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 
                    
                    else :
                        liB[i][j] = 'B'
                        cnB[i + 1][j + 1] = 1 + cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

                else :
                    cnB[i + 1][j + 1] = cnB[i][j + 1] + cnB[i + 1][j] - cnB[i][j] 

if li[0][0] == 'W' : 
    for i in range(N) :
        for j in range(M) :
            if i == 0 and j == 0 :
                continue

            if j != 0 :
                if liW[i][j] == liW[i][j - 1] :
                    if liW[i][j] == 'B' :
                        liW[i][j] = 'W'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 
                    
                    else :
                        liW[i][j] = 'B'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

                else :
                    cnW[i + 1][j + 1] = cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

            else :
                if liW[i - 1][j] == liW[i][j] :
                    if liW[i][j] == 'B' :
                        liW[i][j] = 'W'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 
                    
                    else :
                        liW[i][j] = 'B'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

                else :
                    cnW[i + 1][j + 1] = cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

else :
    liW[0][0] = 'W'
    cnW[1][1] = 1

    for i in range(N) :
        for j in range(M) :
            if i == 0 and j == 0 :
                continue

            if j != 0 :
                if liW[i][j] == liW[i][j - 1] :
                    if liW[i][j] == 'B' :
                        liW[i][j] = 'W'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 
                    
                    else :
                        liW[i][j] = 'B'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

                else :
                    cnW[i + 1][j + 1] = cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

            else :
                if liW[i][j] == liW[i - 1][j] :
                    if liW[i][j] == 'B' :
                        liW[i][j] = 'W'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 
                    
                    else :
                        liW[i][j] = 'B'
                        cnW[i + 1][j + 1] = 1 + cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

                else :
                    cnW[i + 1][j + 1] = cnW[i][j + 1] + cnW[i + 1][j] - cnW[i][j] 

ans = 1e9
#print(cnB)
#print(cnW)

for i in range(K, N + 1) :
    for j in range(K, M + 1) :
        x1 = i - K
        y1 = j - K
        x2 = i
        y2 = j

        ansB = cnB[x2][y2] - cnB[x1][y2] - cnB[x2][y1] + cnB[x1][y1]
        ansW = cnW[x2][y2] - cnW[x1][y2] - cnW[x2][y1] + cnW[x1][y1]
        #print(ansB, ansW)
        ans = min(ans, ansB, ansW)
    
print(ans)