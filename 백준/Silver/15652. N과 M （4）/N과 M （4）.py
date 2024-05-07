N, M = map(int, input().split())

ans = []

def back(n) :
    if n == M :
        for i in ans :
            print(i, end = ' ')
        print()     
        ans.pop()

    else :
        for i in range(1, N + 1) :
            if not ans :
                push(i, n)
            
            else :
                if ans[-1] <= i :
                    push(i, n)
        if ans :
            ans.pop()

def push(i, n) :
    ans.append(i)
    back(n + 1)

back(0)