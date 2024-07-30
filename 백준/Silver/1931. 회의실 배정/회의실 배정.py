N = int(input())
li = []

for i in range(N) :
    li.append(list(map(int, input().split())))

li = sorted(li, key = lambda x : (x[1], x[0]))

ans = 0

#print(li)

t = 0

for i in range(N) :
    if li[i][0] < t : continue
    ans += 1
    t = li[i][1]

print(ans)