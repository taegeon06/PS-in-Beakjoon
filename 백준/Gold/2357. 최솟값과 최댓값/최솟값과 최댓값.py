n, m = map(int, input().split())

def seg_sum(node, s, e, l, r) :
    if s > r or e < l : return 1000000000, 1
    if s <= l and e >= r : return mintree[node], maxtree[node]

    mid = (l + r) // 2

    minnode1, maxnode1 = seg_sum(node * 2, s, e, l, mid)
    minnode2, maxnode2 = seg_sum(node * 2 + 1, s, e, mid + 1, r)

    return min(minnode1, minnode2), max(maxnode1, maxnode2)

t = 1
times = 1

while n > t :
    t = (1 << times) 
    times += 1

maxtree = [1 for i in range(t * 2)]
mintree = [1000000000 for i in range(t * 2)]

for i in range(n) :
    node = int(input())
    maxtree[i + t] = node
    mintree[i + t] = node

#print(maxtree, mintree)

for i in range(t - 1, 0, -1) :
    maxtree[i] = max(maxtree[i * 2], maxtree[i * 2 + 1])
    mintree[i] = min(mintree[i * 2], mintree[i * 2 + 1])

    #print(i, maxtree[i], mintree[i])

#print(maxtree, mintree)

for i in range(m) :
    a, b = map(int, input().split())

    mi, mx = seg_sum(1, a - 1, b - 1, 0, t - 1)

    print(mi, mx)