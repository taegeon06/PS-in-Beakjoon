import sys

input = sys.stdin.readline

n, k = map(int, input().split())

t = 1

while n > t :
    t *= 2

def seg(i, s, e, v) :
    if s == e : return s

    mid = (s + e) // 2

    if tree[i * 2] >= v : 
        return seg(i * 2, s, mid, v)
    
    else :
        return seg(i * 2 + 1, mid + 1, e, v - tree[i * 2])

def query(i, s, e, l, r) :
    if s > r or e < l : return 0
    if s <= l and e >= r : return tree[i]
    
    mid = (l + r) // 2

    v1 = query(i * 2, s, e, l, mid)
    v2 = query(i * 2 + 1, s, e, mid + 1, r)

    return v1 + v2

def update(i) :
    i += t
    tree[i] = 0

    while i > 1 :
        i //= 2
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

tree = [0 for i in range(t * 2)]

for i in range(t + n - 1, 0, -1) :
    if t - 1 < i and i <= t + n - 1 :
        tree[i] = 1

    else :
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

idx = k - 1

print("<", end = '')

if n == 1 :
    print(1, end = '>')

else :
    while tree[1] != 0 :
        v = seg(1, 0, t - 1, idx + 1)

    #print(tree)

    #print(v)

        print(v + 1, end = '')
        if tree[1] != 1 :
            print(', ', end = '')

        update(v)
        #print(tree)

        idx += k - 1

        if idx > tree[1] - 1 and tree[1] != 0 :
            idx -= tree[1] * (idx // tree[1])
        


    print(">")