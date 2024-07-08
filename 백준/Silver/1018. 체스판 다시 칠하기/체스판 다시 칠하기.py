def bruteforce() :
    global count , right
    count = 0
    Mcount = 64
    for down in range(0, (N - 7)) :
        for right in range(0, (M - 7)) :
            for i in range(down, down + 8) :
                for j in range(right, right + 8) :
                    if (S[down][right] == 'W') :
                        if ((i - down) % 2 == 0) :
                            white(i, j)
                        else :
                            black(i, j)
                    
                    else : 
                        if ((i - down) % 2 == 0) :
                            black(i, j)
                        else :
                            white(i, j)
                    #print(i, j,S[i][j], S[down][right] , i - down, j - right,count)

            Mcount = min(Mcount, count)
            count = 0
            for i in range(down, down + 8) :
                for j in range(right, right + 8) :
                    if (S[down][right] != 'W') :
                        if ((i - down) % 2 == 0) :
                            white(i, j)
                        else :
                            black(i, j)
                    
                    else : 
                        if ((i - down) % 2 == 0) :
                            black(i, j)
                        else :
                            white(i, j)

            Mcount = min(Mcount, count)
            count = 0
            

    return Mcount

def white(i, j) :
    global count
    if ((j - right) % 2 == 0) :
        if (S[i][j] != 'W') : count += 1
    else :
        if (S[i][j] != 'B') : count += 1

def black(i, j) :
    global count
    if ((j - right) % 2 == 0) :
        if (S[i][j] != 'B') : count += 1
    else :
        if (S[i][j] != 'W') : count += 1


N, M = map(int, input().split())

S = []
for i in range(N) :
    S.append(list(input()))

print(bruteforce())
