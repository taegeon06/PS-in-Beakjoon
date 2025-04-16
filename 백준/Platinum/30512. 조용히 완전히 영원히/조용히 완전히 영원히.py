import sys

input = sys.stdin.readline

class node :
    def __init__(self, v, c):
        self.v = v
        self.c = c

n = int(input())
a = list(map(int, input().split()))
q = int(input())

d = [0 for i in range(q)]

t = 1

while n > t :
    t *= 2

def lazy(i, s, e, l, r, x, n) :
    if s > r or e < l : return 
    if s <= l and e >= r : 
        if tr[i].v > x :
            tr[i].v = x
            tr[i].c = n

        return
        
    m = (l + r) // 2

    lazy(i * 2, s, e, l, m, x, n)
    lazy(i * 2 + 1, s, e, m + 1, r, x, n)

def find(i, v) :
    i += t
    d = 0

    while i >= 1 :
        if tr[i].v != 1e9 :
            if tr[i].v < v :
                d = tr[i].c
                v = tr[i].v
            
            if tr[i].v == v and d > tr[i].c :
                d = tr[i].c

        i //= 2

    return v, d

tr = [node(1e9, 0) for i in range(t * 2)]

for i in range(q) :
    l, r, x = map(int, input().split())

    lazy(1, l - 1, r - 1, 0, t - 1, x, i)

for i in range(n) :
    #print(tr[i + t].v, end = ' ')
    v, idx = find(i, a[i])
    
    d[idx] += 1
    print(v, end = ' ')

print()

for i in range(1, q) :
    d[i] += d[i - 1]

for i in d :
    print(i, end = ' ')