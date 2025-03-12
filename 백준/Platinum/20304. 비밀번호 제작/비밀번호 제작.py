from collections import deque
import sys

input = sys.stdin.readline

qu = deque()

# i refered blog.encrypted.gg && https://buly.kr/28sxxO2 && https://www.geeksforgeeks.org/binary-formula/ && https://hsyaloe.tistory.com/163 && github.com/encrypted-def/basic-algo-lecture

def BFS() : 
    ans = 0
    while qu :
        X = qu.pop()

        for i in range(20) :
            if X & (1 << i) :
                nx = X & ~(1 << i)

            else :
                nx = X | (1 << i)
            
            if nx > N : continue
            if vi[nx] >= 0 : continue
            
            vi[nx] = vi[X] + 1
            ans = max(ans, vi[nx])
            qu.appendleft(nx)
    
    return ans
N = int(input())
M = int(input())
p = list(map(int, input().split()))
vi = [-1 for i in range(N + 1)]

for i in range(M) :
    vi[p[i]] = 0
    qu.appendleft(p[i])
    #print(len(bin(N)), len(bin(p[i])))

print(BFS())