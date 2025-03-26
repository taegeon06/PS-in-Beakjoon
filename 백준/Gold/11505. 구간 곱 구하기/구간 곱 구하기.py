from math import trunc
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

    mid = trunc((start + end) / 2)
    return seg_sum(node * 2, start, mid, left, right) * seg_sum(node * 2 + 1, mid + 1, end, left, right)

def seg_update(idx, val) :
    idx += t
    tree[idx] = val

    while idx > 1 :
        idx = trunc(idx / 2)
        tree[idx] = tree[idx * 2] % mod * tree[idx * 2 + 1] % mod

times = 2

while n > t :
    t *= times

tree = [1 for i in range(t * 2)]

for i in range(n) :
    val = int(input())
    seg_update(i, val)

#print(tree)

for i in range(m + k) :
    a, b, c = map(int, input().split())

    if a == 1 :
        seg_update(b - 1, c)
    
    if a == 2 :
        print(seg_sum(1, 0, t - 1, b - 1, c - 1) % mod)
        
    #print(tree)