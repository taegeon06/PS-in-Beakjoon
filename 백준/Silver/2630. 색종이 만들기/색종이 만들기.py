n = int(input())

ai = [list(map(int, input().split())) for i in range(n)]
cnt = [0, 0]

def division(sx, sy, ex, ey) :
    if sx == ex and sy == ey : 
        cnt[ai[sx][sy]] += 1
        return
    
    else :
        di = False
        st = ai[sx][sy]

        for i in range(sx, ex) :
            if di : break

            for j in range(sy, ey) :
                if st != ai[i][j] :
                    di = True
                    break
                
        if di :
            if ex - sx == 1 and ey - sy == 1 :
                division(sx, sy, sx, sy)
                division(sx, ey, sx, ey)
                division(ex, sy, ex, sy)
                division(ex, ey, ex, ey)

            if ex - sx > 1 and ey - sy > 1:
                '''if sx == 0 and sy == 0 and ey == n and ex == n : 
                    print((ex - sx) // 2)'''

                division(sx, sy, (ex - sx) // 2 + sx, (ey - sy) // 2 + sy)
                division((ex - sx) // 2 + sx, sy, ex,  (ey - sy) // 2 + sy)
                division(sx, (ey - sy) // 2 + sy, (ex - sx) // 2 + sx, ey)
                division((ex - sx) // 2 + sx, (ey - sy) // 2 + sy, ex, ey)

        else :
            cnt[st] += 1
            return
            
division(0, 0, n, n)
print(cnt[0])
print(cnt[1])