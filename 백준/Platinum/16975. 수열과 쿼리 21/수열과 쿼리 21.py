n = int(input())

ai = list(map(int, input().split()))
m = int(input())

t = 1

while n > t :
    t *= 2
    
def query(i, s, e, l, r, v) :
    if s > r or e < l : return 0
    if s <= l and e >= r : 
        tree1[i] += v
        return tree[i]

    mid = (l + r) // 2

    query(i * 2, s, e, l, mid, v)
    query(i * 2 + 1, s, e, mid + 1, r, v)

def update(i) :
    k = 0
    i += t - 1
    k += tree1[i]

    while i > 1 :
        i //= 2
        k += tree1[i]
    
    return k
        

tree = [0 for i in range(t * 2)]
tree1 = [0 for i in range(t * 2)]

for i in range(n) :
    tree[i + t] = ai[i]

for i in range(t - 1, 0, -1) :
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

for i in range(m) :
    q = list(map(int, input().split()))

    if q[0] == 1 :
        query(1, q[1] - 1, q[2] - 1, 0, t - 1, q[3])
    
    if q[0] == 2 :
        print(tree[q[1] - 1 + t] + update(q[1]))