n = int(input())
ai = list(map(int, input().split()))
m = int(input())

t = 1

while n > t :
    t *= 2

def seg(i, v, s, e) :
    if s == e : return s

    m = (s + e) // 2

    if tree[i * 2] >= v :
        return seg(i * 2, v, s, m)

    else :
        return seg(i * 2 + 1, v - tree[i * 2], m + 1, e)


def update(i, v) :
    i += t - 1
    tree[i] += v

    while i > 1 :
        i //= 2
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

tree = [0 for i in range(t * 2)]

for i in range(n) :
    tree[i + t] = ai[i]

for i in range(t - 1, 0, -1) :
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

#print(tree)
#print(query(1, 0, -1, 0, t - 1))
for i in range(m) :
    q = list(map(int, input().split()))

    if q[0] == 1 :
        update(q[1], q[2])
    
    if q[0] == 2 :
        #print(tree)
        print(seg(1, q[1], 0, t - 1) + 1)
        #print('ok')