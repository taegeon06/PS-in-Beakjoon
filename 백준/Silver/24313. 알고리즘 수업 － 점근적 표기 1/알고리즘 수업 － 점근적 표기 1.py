a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

fi = True

for n in range(n0, 101) :
    if a1 * n + a0 > c * n :
        fi = False
    
if fi :
    print(1)

else :
    print(0)