n, m = map(int, input().split())

a = []

for i in range(n) :
    a.append(int(input()))

t = 1

while n > t :
    t *= 2

def query(i, s, e, l, r) :
    if s > r or e < l : return 10 ** 9
    if s <= l and e >= r : return tr[i]

    m = (l + r) // 2

    v1 = query(i * 2, s, e, l, m)
    v2 = query(i * 2 + 1, s, e, m + 1, r)

    return min(v1, v2)

tr = [10 ** 9 for i in range(t * 2)]

for i in range(n) :
    tr[i + t] = a[i]

for i in range(t - 1, 0, -1) :
    tr[i] = min(tr[i * 2], tr[i * 2 + 1])

for i in range(m) :
    a, b = map(int, input().split())
    print(query(1, a - 1, b - 1, 0, t - 1))