li = list(input())

st = 0

an = []
temp = []

l = len(li)

for i in range(l) :
    if li[i] == '+' or li[i] == '-' :
        an.append(''.join(temp))
        an.append(li[i])
        temp.clear()
    
    else :
        temp.append(li[i])

an.append(''.join(temp))

for i in range(len(an)) :
    if an[i] == '+' or an[i] == '-' :
        continue
    
    else :
        an[i] = int(an[i])

temp = an[0]
li.clear()

for i in range(len(an) - 1) :
    if an[i] == '+' :
        temp += an[i + 1]

    elif an[i] == '-' :
        li.append(temp)
        temp = an[i + 1]

li.append(temp)

if len(li) != 1 :
    ans = li[0]
    for i in range(1, len(li)) :
        ans -= li[i]

    print(ans)

else :
    print(li[-1])