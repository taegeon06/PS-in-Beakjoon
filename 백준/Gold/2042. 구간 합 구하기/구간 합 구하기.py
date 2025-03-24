from math import trunc

n, m, k = map(int, input().split())
arr = [0]
tree = [0 for i in range(n * 10)]
#(1 << ceil(log(n + 1)) + 1) + 1 + 1

for i in range(n) :
    arr.append(int(input()))

#arr.sort()
#print(arr)

def seg(node, start, end) :
    if start == end :
        tree[node] = arr[start]
        return tree[node]
    
    tree[node] = seg(node * 2, start, trunc((start + end) / 2)) + seg(node * 2 + 1, trunc((start + end) / 2) + 1, end)
    return tree[node]

def seg_sum(node, start, end, left, right) :
    if right < start or left > end : return 0

    if left <= start and right >= end :
        return tree[node]
    
    return seg_sum(node * 2, start, trunc((start + end) / 2), left, right) + seg_sum(node * 2 + 1, trunc((start + end) / 2) + 1, end, left, right)

def seg_update(node, start, end, idx, diff) :
    if idx < start or idx > end : return
    tree[node] += diff

    if start != end : 
        seg_update(node * 2, start, trunc((start + end) / 2), idx, diff)
        seg_update(node * 2 + 1, trunc((start + end) / 2) + 1, end, idx, diff)



seg(1, 1, n)

for i in range(m + k) :
    a, b, c = map(int, input().split())

    #print(tree)
    if a == 1 : 
        diff = c - arr[b]
        arr[b] = c
        seg_update(1, 1, n, b, diff)
    
    if a == 2 : 
        #print(b, c)
        print(seg_sum(1, 1, n, b, c))