N = int(input())
li = list(map(int, input().split()))
li.reverse()

temp = []
ord = 1
#print(li)
for i in range(N) :
    #print(temp)
    ps = li.pop()
    if ps != ord :
        temp.append(ps)

    else :
        ord += 1

    if temp :
        tmp = len(temp)
        for j in range(tmp) :
            if temp[-1] == ord :
                temp.pop()
                ord += 1
            else :
                break

if temp :
    print("Sad")
else :
    print("Nice")