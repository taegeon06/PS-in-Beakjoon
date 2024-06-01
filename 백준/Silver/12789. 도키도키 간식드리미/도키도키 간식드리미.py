import sys

input = sys.stdin.readline

N = int(input())

order = []

for i in range(1,N + 1) :
    order.append(i)

J = list(map(int,input().split()))
J.reverse()

space = []
index = 0

while J :
    if J[-1] == order[index] :
        J.pop()
        index += 1
    else :
        if space and space[-1] == order[index] :
            space.pop()
            index += 1
        else :
            space.append(J.pop())

while space :
    if space[-1] == order[index] :
        space.pop()
        index += 1
    else :
        break

if not J and not space :
    print('Nice')
else : print('Sad')


    
    


