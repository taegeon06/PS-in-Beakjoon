a = []
n = int(input())

for i in range(n) :
    s = input().split()

    if s[0] == 'push' :
        a.append(int(s[1]))
    
    elif s[0] == 'pop' :
        if a :
            print(a.pop())
        
        else :
            print(-1)
        
    elif s[0] == 'size' :
        print(len(a))
    
    elif s[0] == 'empty' :
        if a :
            print(0)
        
        else :
            print(1)
        
    else :
        if a :
            print(a[-1])
        
        else :
            print(-1)