n = int(input())
ai = list(map(int, input().split()))
m = int(input())

t = 1

while n > t :
    t *= 2

def update(i, v) :
    i += t - 1
    tree[i] = v

    while i > 1 :
        i //= 2

        if tree[i * 2] > tree[i * 2 + 1] :
            tree[i] = tree[i * 2 + 1]
            tree1[i] = tree1[i * 2 + 1]
    
        elif tree[i * 2] < tree[i * 2 + 1] :
            tree[i] = tree[i * 2]
            tree1[i] = tree1[i * 2]
    
        else :  
            if tree1[i * 2] > tree1[i * 2 + 1] :
                tree[i] = tree[i * 2]
                tree1[i] = tree1[i * 2 + 1]
        
            else :
                tree[i] = tree[i * 2]
                tree1[i] = tree1[i * 2]

        

tree = [1e9 for i in range(t * 2)]
tree1 = [0 for i in range(t * 2)]

for i in range(n) :
    tree[i + t] = ai[i]
    tree1[i + t] = i + 1

for i in range(t - 1, 0, -1) :
    if tree[i * 2] > tree[i * 2 + 1] :
        tree[i] = tree[i * 2 + 1]
        tree1[i] = tree1[i * 2 + 1]
    
    elif tree[i * 2] < tree[i * 2 + 1] :
        tree[i] = tree[i * 2]
        tree1[i] = tree1[i * 2]
    
    else :  
        if tree1[i * 2] > tree1[i * 2 + 1] :
            tree[i] = tree[i * 2]
            tree1[i] = tree1[i * 2 + 1]
        
        else :
            tree[i] = tree[i * 2]
            tree1[i] = tree1[i * 2]

#print(tree)

for i in range(m) :
    q = list(map(int, input().split()))

    if q[0] == 1 :
        update(q[1], q[2])
        #print(tree)
    
    if q[0] == 2 :
        print(tree1[1])