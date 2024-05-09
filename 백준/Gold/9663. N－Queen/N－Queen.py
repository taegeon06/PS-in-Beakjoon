import sys

input = sys.stdin.readline

N = int(input().rstrip())

cnt = 0
queen = []
isused1 = []
isused2 = []
isused3 = []
for i in range(31) :
    isused1.append(False)
    isused2.append(False)
    isused3.append(False)
        

def back(k) :
    global cnt
    if k == N :
        cnt += 1
        return
    
    else :
        for i in range(N) :
            if not isused1[i] and not isused2[i + k] and not isused3[k - i + N - 1] :
                isused1[i] = isused2[i + k] = isused3[k - i + N - 1] = True
                back(k + 1)
                isused1[i] = isused2[i + k] = isused3[k - i + N - 1] = False

    
back(0)
print(cnt)