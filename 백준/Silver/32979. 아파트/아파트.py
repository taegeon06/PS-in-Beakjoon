from collections import deque

n = int(input())
t = int(input())

a = deque(map(int, input().split()))
b = list(map(int, input().split()))

idx = 0

for i in range(t) :
    for j in range(b[i] - 1) :
        tm = a.popleft()
        a.append(tm)
    
    print(a[0], end = ' ')