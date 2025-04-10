import sys

input = sys.stdin.readline

class node :
    def __init__(self, v, l):
        self.v = v
        self.l = l
    
n = int(input())
ai = list(map(int, input().split()))
m = int(input())

t = 1

while n > t :
    t *= 2

def lazy(i, s, e, l, r, x) :
    if tr[i].l != -1 :
        if (l - r + 1) % 2 != 0 :
            tr[i].v ^= tr[i].l

        if i < t :
            if tr[i * 2].l == -1 :
                tr[i * 2].l = tr[i].l
            else :
                tr[i * 2].l ^= tr[i].l
            
            if tr[i * 2 + 1].l == -1 :
                tr[i * 2 + 1].l = tr[i].l
            
            else :
                tr[i * 2 + 1].l ^= tr[i].l
        
        tr[i].l = -1
    
    if s > r or e < l : return 0
    if s <= l and e >= r :
        if (l - r + 1) % 2 != 0 :
            tr[i].v ^= x

        if i < t :
            if tr[i * 2].l == -1 :
                tr[i * 2].l = x

            else :
                tr[i * 2].l ^= x
            
            if tr[i * 2 + 1].l == -1 :
                tr[i * 2 + 1].l = x
            
            else :
                tr[i * 2 + 1].l ^= x
        
        return tr[i].v

    m = (l + r) // 2

    v1 = lazy(i * 2, s, e, l, m, x)
    v2 = lazy(i * 2 + 1, s, e, m + 1, r, x)

    tr[i].v = tr[i * 2].v ^ tr[i * 2 + 1].v

    return v1 ^ v2

def query(i, s, e, l, r) :
    if tr[i].l != -1 :
        if (l - r + 1) % 2 != 0 :
            tr[i].v ^= tr[i].l

        if i < t :
            if tr[i * 2].l == -1 :
                tr[i * 2].l = tr[i].l
            else :
                tr[i * 2].l ^= tr[i].l
            
            if tr[i * 2 + 1].l == -1 :
                tr[i * 2 + 1].l = tr[i].l
            
            else :
                tr[i * 2 + 1].l ^= tr[i].l
        
        tr[i].l = -1
    
    if s > r or e < l : return 0
    if s <= l and e >= r : return tr[i].v

    m = (l + r) // 2

    v1 = query(i * 2, s, e, l, m)
    v2 = query(i * 2 + 1, s, e, m + 1, r)

    return v1 ^ v2

tr = [node(-1, 0) for i in range(t * 2)]

for i in range(n) :
    tr[i + t].v = ai[i]

for i in range(t - 1, 0, -1) :
    tr[i].v = tr[i * 2].v ^ tr[i * 2 + 1].v

for i in range(m) :
    q = list(map(int, input().split()))

    if q[0] == 1 :
        lazy(1, q[1], q[2], 0, t - 1, q[3])
    
    if q[0] == 2 :
        print(query(1, q[1], q[2], 0, t - 1))