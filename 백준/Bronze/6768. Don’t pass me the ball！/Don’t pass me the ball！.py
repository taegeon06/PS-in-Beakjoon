j = int(input())

cnt = 0

if 3 > j :
    print(cnt)

else :
    for i in range(1, j - 2) :
        for k in range(i + 1, j - 1) :
            for l in range(k + 1, j) :
                cnt += 1

    print(cnt)