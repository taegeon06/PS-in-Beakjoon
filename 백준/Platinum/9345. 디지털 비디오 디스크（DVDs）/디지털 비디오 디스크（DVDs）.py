
import sys

input = sys.stdin.readline

T = int(input())

def query(i, s, e, l, r) :
    if s > r or e < l : return 0, n - 1
    if s <= l and e >= r : return tree[i], tree1[i]

    mid = (l + r) // 2

    v1, v11 = query(i * 2, s, e, l, mid)
    v2, v22 = query(i * 2 + 1, s, e, mid + 1, r)

    return max(v1, v2), min(v11, v22)

def update(i, v, v1) :
    i += t
    tree[i] = v
    tree1[i] = v1

    while i > 1 :
        i //= 2
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        tree1[i] = min(tree1[i * 2], tree1[i * 2 + 1])


for _ in range(T) :
    n, k = map(int, input().split())

    t = 1

    while n > t :
        t *= 2

    tree = [0 for i in range(t * 2)]
    tree1 = [n - 1 for i in range(t * 2)]

    for i in range(n) :
        tree[i + t] = i
        tree1[i + t] = i

    
    for i in range(t - 1, 0, -1) :
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        tree1[i]= min(tree1[i * 2], tree1[i * 2 + 1])
    
    #print(tree, ai)

    for i in range(k) :
        q, a, b = map(int, input().split())

        if q == 0 :
            v1 = tree[a + t]
            v11 = tree1[a + t]
            v2 = tree[b + t]
            v22 = tree1[b + t]
            update(a, v2, v22)
            update(b, v1, v11)
        
        if q == 1 :
            v1, v2 = query(1, a, b, 0, t - 1)

            if v1 == b and v2 == a :
                print("YES")
            
            else :
                print("NO")
            
            #print(v11, v22, a, b)
            #print(tree, tree1, tree2, tree3)```