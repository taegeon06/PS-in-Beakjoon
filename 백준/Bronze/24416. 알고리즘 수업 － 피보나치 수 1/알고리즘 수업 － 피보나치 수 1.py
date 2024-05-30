N = int(input())

cnt1 = 0
cnt2 = 0

def fi1(n) :
    global cnt1
    if n == 1 or n == 2 :
        cnt1 += 1
        return 1
    
    else :
        return fi1(n - 1) + fi1(n - 2)
    
def fi2(n) :
    global cnt2
    for i in range(3, n + 1) :
        cnt2 += 1
    return cnt2

print(fi1(N), fi2(N))
