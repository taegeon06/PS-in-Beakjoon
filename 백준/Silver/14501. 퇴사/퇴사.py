N = int(input())
li = [[0, 0] for i in range(21)]

for i in range(1, N + 1) :
    T, P = map(int, input().split())
    li[i] = [T, P]

vi = [False for i in range(21)]

ma = 0
sum = 0

def back(k) :
    #print(k)
    global sum, ma
    if k + li[k][0] > N + 1:
        #print(sum)
        #print('pass')
        ma = max(ma ,sum)
        if k < N + 1 :
            back(k + 1)

    elif k + li[k][0] == N + 1 :
        ma = max(ma, sum + li[k][1])
        back(k + 1)

    else :
        for i in range(k, N + 1) :
            if vi[i] == False and i + li[i][0] <= N + 1 :
                #print('pass', i)
                sum += li[i][1]
                vi[i] = True
                back(i + li[i][0])
                sum -= li[i][1]            
                vi[i] = False

back(1)
print(ma)