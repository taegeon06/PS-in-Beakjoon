import sys

#드디어 ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ

input = sys.stdin.readline

n, m, k = map(int, input().split())
t = 1
mod = 1000000007

def seg_sum(node, start, end, left, right) :
    if right < start or left > end : return 1

    if left <= start and right >= end :
        #print(start, end, tree[node], node)
        return tree[node]

    mid = (start + end) // 2
    node1 = seg_sum(node * 2, start, mid, left, right)
    node2 = seg_sum(node * 2 + 1, mid + 1, end, left, right)
    return (node1 * node2) % mod

def seg_update(idx, val) :
    idx += t
    tree[idx] = val

    while idx > 1 :
        idx //= 2
        tree[idx] = (tree[idx * 2] * tree[idx * 2 + 1]) % mod

while n > t :
    t *= 2

tree = [1 for i in range(t * 2)]

for i in range(n) :
    tree[t + i] = int(input())

for i in range(t - 1, 0, -1) :
    tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % mod

#print(tree)

for i in range(m + k) :
    a, b, c = map(int, input().split())

    if a == 1 :
        seg_update(b - 1, c)
    
    if a == 2 :
        print(seg_sum(1, 0, t - 1, b - 1, c - 1))
        
    #print(tree)