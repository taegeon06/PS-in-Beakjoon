t = int(input())

a = 60 * 5
b = 60
c = 10

ac = 0
bc = 0
cc = 0

if c > t :
    print(-1)

else :
    f = 0
    if t >= a :
        ac += t // a
        t -= a * (t // a)
        
    if t >= b :
        bc += t // b
        t -= b * (t // b)
    
    if t >= c :
        cc += t // c
        t -= c * (t // c)
        
    
    if t == 0 :
        print(ac, bc, cc)

    else :
        print(-1)