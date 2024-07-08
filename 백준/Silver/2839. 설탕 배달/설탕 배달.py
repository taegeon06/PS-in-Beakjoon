N = int(input())

count_5 = 0
count_3 = 0

count = 5000

for i in range(1001) :
    for j in range(1001) :
        Nf = N
        N -= 5 * i
        if (N != 0) : N -= 3 * j
        
        if (N == 0) :
            count = min(count, i + j)
        N = Nf
if count == 5000 :
    print(-1)
else : print(count)
