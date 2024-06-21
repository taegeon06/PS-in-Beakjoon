N, M = map(int, input().split())
A, B = map(int, input().split())
    
#print(li)    

for i in range(M) :
    K = int(input())

    if A <= K :
        temp = A
        A = B
        B = temp

print(A)