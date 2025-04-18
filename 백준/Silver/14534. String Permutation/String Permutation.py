t = int(input())

def back(i, v, s) :
    if i == v :
        tm = ''
        for j in range(len(s)) :
            tm += a[s[j]] 
        print(tm)
        return
    
    else :
        for j in range(v) :
            f = 0
            for k in range(len(s)) :
                if j == s[k] :
                    f = 1
                    break
            
            if f == 1 : continue

            else :
                s.append(j)
                back(i + 1, v, s)
                s.pop()

for i in range(t) :
    a = list(input())

    print('Case # %d:' % (i + 1))
    for j in range(len(a)) :
        back(1, len(a), [j])