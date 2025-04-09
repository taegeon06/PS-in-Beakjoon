class node :
    def __init__(self, v, l):
        self.v = v
        self.l = l

n, m = map(int, input().split())

t = 1

while n > t :
    t *= 2

def lazy(i, s, e, l, r) :
    if tr[i].l != 0 :
        tr[i].v = 1 * (r - l + 1) - tr[i].v

        if i < t : 
            if tr[i * 2].l == 1 :
                tr[i * 2].l = 0
            
            else :
                tr[i * 2].l = 1
            
            if tr[i * 2 + 1].l == 1 :
                tr[i * 2 + 1].l = 0 
            
            else :
                tr[i * 2 + 1].l = 1
            
        tr[i].l = 0
    
    if s > r or e < l : return 0
    if s <= l and e >= r :
        tr[i].v = 1 * (r - l + 1) - tr[i].v

        if i < t : 
            if tr[i * 2].l == 1 :
                tr[i * 2].l = 0
            
            else :
                tr[i * 2].l = 1
            
            if tr[i * 2 + 1].l == 1 :
                tr[i * 2 + 1].l = 0 
            
            else :
                tr[i * 2 + 1].l = 1

        return tr[i].v
    
    m = (l + r) // 2

    lazy(i * 2, s, e, l, m)
    lazy(i * 2 + 1, s, e, m + 1, r)

    tr[i].v = tr[i * 2].v + tr[i * 2 + 1].v

    return tr[i].v

def query(i, s, e, l, r) :
    if tr[i].l != 0 :
        tr[i].v = 1 * (r - l + 1) - tr[i].v

        if i < t : 
            if tr[i * 2].l == 1 :
                tr[i * 2].l = 0
            
            else :
                tr[i * 2].l = 1
            
            if tr[i * 2 + 1].l == 1 :
                tr[i * 2 + 1].l = 0 
            
            else :
                tr[i * 2 + 1].l = 1
            
        tr[i].l = 0

    if s > r or e < l : return 0
    if s <= l and e >= r : return tr[i].v

    m = (l + r) // 2

    v1 = query(i * 2, s, e, l, m)
    v2 = query(i * 2 + 1, s, e, m + 1, r)

    return v1 + v2

tr = [node(0, 0) for i in range(t * 2)]

for i in range(m) :
    o, s, T = map(int, input().split())
    
    if o == 0 :
        lazy(1, s - 1, T - 1, 0, t - 1)
    
    if o == 1 :
        print(query(1, s - 1, T - 1, 0, t - 1))
    
    '''for j in range(t * 2) :
        print(tr[j].v, end = " ")
    
    print()
    
    for j in range(t * 2) :
        print(tr[j].l, end = ' ')
    
    print('ok')'''