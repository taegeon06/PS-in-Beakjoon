from itertools import permutations

t = int(input())

for i in range(t) :
    a = list(input())

    v = list(permutations(a, len(a)))
    
    print('Case # %d:' % (i + 1))

    for i in range(len(v)) :
        t = ''.join(v[i])
        print(t)