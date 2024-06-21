N, M = map(int, input().split())
li = []

for i in range(N) :
    A, B = map(int, input().split())

    li.append([A, B])
    
#print(li)    

for i in range(M) :
    K = int(input())

    for j in range(N) :
        if li[j][0] <= K :
            temp = li[j][0]
            li[j][0] = li[j][1]
            li[j][1] = temp

sum = 0

for i in range(N) :
    sum += li[i][0]

print(sum)