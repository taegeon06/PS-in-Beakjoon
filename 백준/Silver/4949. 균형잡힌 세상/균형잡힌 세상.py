from collections import deque
import sys

input = sys.stdin.readline

string = list(input().rstrip())


while string[0] != '.':
    stack = deque()
    for str in string :
        if str == '(' or str == '[' or str == '{':
            stack.append(str)
        if str == ')' or str == ']' or str == '}':
            if not stack : 
                stack.append('0')
                break
            if stack[-1] + str== '()' or stack[-1] + str == '[]' or stack[-1] + str == '{}':
                stack.pop()
            else : 
                stack.append('0')
                break
        
    if stack :
        print("no")
    else :
        print("yes")
    
    string = list(input().rstrip())