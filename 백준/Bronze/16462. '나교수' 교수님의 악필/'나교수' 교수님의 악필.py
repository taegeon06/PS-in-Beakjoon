import math

N = int(input())

sum = 0
for i in range(N) :
    q = list(input())

    for j in range(len(q)) :
        if q[j] == '0' or q[j] == '6' :
            q[j] = '9'

    temp = int(''.join(q))
    
    if temp > 100 :
        temp = 100

    #print("temp = %d" %(temp))
    
    sum += temp
    #print("sum = %d" %(sum))
#print(sum / N)
if sum / N - math.trunc(sum / N) >= 0.5 :
    ans = math.ceil(sum / N)

else :
    ans = math.floor(sum / N)

print(ans)