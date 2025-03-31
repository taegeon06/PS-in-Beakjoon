n = int(input())
ai = list(map(int, input().split()))
m = int(input())

t = 1

while n > t :
    t *= 2

def seg(i, v, s, e) :
    mid = (s + e) // 2

    if i * 2 >= t :
        idx = i * 2

        v1 = tree[idx] + query(1, 0, idx - t - 1, 0, t - 1)
        v2 = tree[idx + 1] + query(1, 0, idx - t, 0, t - 1)

        if v <= v1 : 
            #print(idx - t, tree[idx], v)
            return idx - t
        if v > v1 and v <= v2 : 
            #print(idx + 1 - t, tree[idx + 1], v)
            return idx + 1 - t 
    
    else :
        v1 = tree[i * 2] + query(1, 0, s - 1, 0, t - 1)
        v2 = tree[i * 2 + 1] + query(1, 0, mid, 0, t - 1)


        #print(v1, v2, tree[i * 2 + 1], v)

        if v <= v1 : 
            #print(1)
            return seg(i * 2, v, s, mid)

        if v > v1 and v <= v2 :
            #print(2)
            return seg(i * 2 + 1, v, mid + 1, e)
    
def query(i, s, e, l, r) :
    if s > r or e < l : return 0
    if s <= l and e >= r : return tree[i]

    mid = (l + r) // 2

    v1 = query(i * 2, s, e, l, mid)
    v2 = query(i * 2 + 1, s, e, mid + 1, r)

    return v1 + v2


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