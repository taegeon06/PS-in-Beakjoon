N = int(input())

for i in range(N) :
    li = input()
    ans = [0 for i in range(8)]
    st = 0
    ed = 3
    while st != 38 :
        #print("li[st : en] = %s" %(li[st : ed]))
        if li[st : ed] == 'TTT' :
            ans[0] += 1
        
        elif li[st : ed] == 'TTH' :
            ans[1] += 1

        elif li[st : ed] == 'THT' :
            ans[2] += 1

        elif li[st : ed] == 'THH' :
            ans[3] += 1
        
        elif li[st : ed] == 'HTT' :
            ans[4] += 1

        elif li[st : ed] == 'HTH' :
            ans[5] += 1

        elif li[st : ed] == 'HHT' :
            ans[6] += 1

        else :
            ans[7] += 1
        
        st += 1
        ed += 1

    for i in ans :
        print(i, end = " ")