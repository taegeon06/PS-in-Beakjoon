n = int(input())

ai = [[int(input()), i] for i in range(n)]
mod = 1000000007
min = ai.copy()

min.sort(key = lambda x : x[0])

for i in range(n) :
    ai[min[i][1]].append(i)

t = 1

#print(ai)

while n > t :
    t *= 2

def query(i, s, e, l, r) :
    if s > r or e < l : return 0
    if s <= l and e >= r : return tree[i]

    mid = (l + r) // 2

    v1 = query(i * 2, s, e, l, mid)
    v2 = query(i * 2 + 1, s, e, mid + 1, r)

    return v1 + v2

def update(i, v) :
    i += t
    tree[i] = v

    while i > 1 :
        i //= 2
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

def query1(i, s, e, l, r) :
    if s > r or e < l : return 0
    if s <= l and e >= r : return tree1[i]

    mid = (l + r) // 2

    v1 = query1(i * 2, s, e, l, mid)
    v2 = query1(i * 2 + 1, s, e, mid + 1, r)

    return v1 + v2

def update1(i, v) :
    i += t
    tree1[i] = v

    while i > 1 :
        i //= 2
        tree1[i] = tree1[i * 2] + tree1[i * 2 + 1]
    
def query2(i, s, e, l, r) :
    if s > r or e < l : return 1
    if s <= l and e >= r : return tree2[i]

    mid = (l + r) // 2

    v1 = query2(i * 2, s, e, l, mid)
    v2 = query2(i * 2 + 1, s, e, mid + 1, r)

    return (v1 * v2) % mod


tree = [0 for i in range(t * 2)]
tree1 = [0 for i in range(t * 2)]
tree2 = [1 for i in range(t * 2)]

for i in range(n) :
    v1 = query(1, ai[i][2] + 1, n - 1, 0, t - 1)
    v2 = query(1, 0, ai[i][2] - 1, 0, t - 1)

    c1 = query1(1, ai[i][2] + 1, n - 1, 0, t - 1)
    c2 = query1(1, 0, ai[i][2] - 1, 0, t - 1)

    #print(v1, v2, c1 * ai[i][0], c2 * ai[i][0])

    tree2[i + t] = (v1 - ai[i][0] * c1) + (ai[i][0] * c2 - v2)

    #if tree2[i + t] == 0 : tree2[i + t] = 1
    
    update(ai[i][2], ai[i][0])
    update1(ai[i][2], 1)
    #print(tree, tree1, tree2)

for i in range(t - 1, 0, -1) :
    tree2[i] = (tree2[i * 2] * tree2[i * 2 + 1]) % mod

print(query2(1, 1, n - 1, 0, t - 1))
#print(tree2)