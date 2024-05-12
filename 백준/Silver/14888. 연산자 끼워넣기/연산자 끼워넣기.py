from math import trunc
import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
cal = list(map(int, input().rstrip().split()))
ans = A[0]
MAX = -1000000000
MIN = 1000000000

def back(k) :
    global ans, MAX, MIN
    if k == N:
        MAX = max(MAX, ans)
        MIN = min(MIN, ans)
    else :
          for i in range(4) :
            if cal[i] != 0:
                if i == 0 :
                    temp = ans
                    ans += A[k]
                    push(i, k)
                    ans = temp
                    
                elif i == 1 :
                    temp = ans
                    ans -= A[k]
                    push(i, k)
                    ans = temp
                
                elif i == 2 :
                    temp = ans
                    ans *= A[k]
                    push(i, k)
                    ans = temp
                
                else :
                    temp = ans
                    ans = trunc(ans / A[k])
                    push(i, k)
                    ans = temp
            

            
            
def push(i, k) :
    cal[i] -= 1
    back(k + 1)
    cal[i] += 1

back(1)
print(MAX)
print(MIN)