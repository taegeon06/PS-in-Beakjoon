n = int(input())
ai = [list(input()) for i in range(n)]

st = []

def divide(sx, sy, ex, ey, nu) :
    di = False
    s = ai[sx][sy]

    for i in range(sx, ex) :
        if di : break

        for j in range(sy, ey) :
            if s != ai[i][j] :
                di = True
                break
    
    if di :
        st.append("(")
        divide(sx, sy, (ex - sx) // 2 + sx, (ey - sy) // 2 + sy, 1)
        divide(sx, (ey - sy) // 2 + sy, (ex - sx) // 2 + sx, ey, 2)
        divide((ex - sx) // 2 + sx, sy, ex, (ey - sy) // 2 + sy, 3)
        divide((ex - sx) // 2 + sx, (ey - sy) // 2 + sy, ex, ey, 4)
        st.append(")")
    
    if not di :
        st.append("%s" % (s))
        return


divide(0, 0, n, n, 0)

for i in st :
    print(i, end = "")