import sys

input = sys.stdin.readline

n = int(input())

mxn = 2 * 1e6

t = 1

while mxn > t :
    t *= 2

def seg(i, v, s, e) :
    if s == e : return s

    m = (s + e) // 2

    if tree[i * 2] >= v :
        return seg(i * 2, v, s, m)
    
    else :
        return seg(i * 2 + 1, v - tree[i * 2], m + 1, e)

def update(i, v) :
    i += t - 1
    tree[i] += v

    while i > 1 :
        i //= 2
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
    
tree = [0 for i in range(t * 2)]

for i in range(n) :
    T, x = map(int, input().split())

    if T == 1 :
        update(x, 1)
        #print(tree[x + t - 1], tree[1])
    
    if T == 2 :
        v = seg(1, x, 0, t - 1) + 1
        print(v)
        update(v, -1)