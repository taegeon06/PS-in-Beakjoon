n = int(input())

mx = [0, 0, 0]
mn = [0, 0, 0]

for i in range(n) :
    a = list(map(int, input().split()))

    if i == 0 :
        mx[0] = a[0]
        mx[1] = a[1]
        mx[2] = a[2]

        mn[0] = a[0]
        mn[1] = a[1]
        mn[2] = a[2]
    
    else :
        mx0 = mx[0]
        mx1 = mx[1]
        mx2 = mx[2]

        mn0 = mn[0]
        mn1 = mn[1]
        mn2 = mn[2]

        #print(a[2], max(mx[1], mx[2]))
        mx[0] = a[0] + max(mx0, mx1)
        mx[1] = a[1] + max(mx0, mx1, mx2)
        mx[2] = a[2] + max(mx1, mx2)

        mn[0] = a[0] + min(mn0, mn1)
        mn[1] = a[1] + min(mn0, mn1, mn2)
        mn[2] = a[2] + min(mn1, mn2)
    
    #print(mx, mn)
print(max(mx), min(mn))
#print(mx, mn)