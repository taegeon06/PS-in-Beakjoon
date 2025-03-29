n = int(input())
ai = list(map(int, input().split()))

arr = [[0, i] for i in range(n)]

for i in range(n) :
    arr[i][0] = ai[i]

arr.sort(key = lambda x : x[0])

#print(arr)

t = 1
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

tree = [0 for i in range(t * 2)]

ans = 0

for i in range(n - 1, -1, -1) :
    v = query(1, 0, arr[i][1] - 1, 0, t - 1)
    ans += v

    #print(tree)

    update(arr[i][1], 1)

    #print(v)

#print(tree)
print(ans)