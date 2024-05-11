import sys
from collections import deque
input = sys.stdin.readline

sto = []
blank = deque()
cnt = 0


for i in range(9) :
    sto.append(list(map(int, input().rstrip().split())))
    for j in range(9) :
        if sto[i][j] == 0 :
            cnt += 1
            blank.append((i, j))


def push(i, j) :
    i3 = (i // 3) * 3
    j3 = (j // 3) * 3
    
    lo = set()

    for k in range(1, 10) :
        lo.add(k)

    for k in range(9) :
        if sto[i][k] in lo :
            lo.remove(sto[i][k])
            
        if sto[k][j] in lo :
            lo.remove(sto[k][j])

    for k in range(i3, i3 + 3) :
        for l in range(j3, j3 + 3) :
            if sto[k][l] in lo :
                lo.remove(sto[k][l])

    return lo

def back(n) :
    if n == cnt :
        for i in range(9) :
            for j in range(9) :
                print(sto[i][j], end = ' ')
            print()
        sys.exit()

    else :
        i, j = blank[n]
        lo = push(i, j)

        for k in lo :
            sto[i][j] = k
            back(n + 1)
            sto[i][j] = 0

back(0)