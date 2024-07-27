import sys

input = sys.stdin.readline

li = list(input())
q = int(input())

ar = {}

def fi(c) :
    temp = [0] * (len(li) + 1)
    for i in range(1, len(li) + 1) :
        if li[i - 1] == c :
            temp[i] = temp[i - 1] + 1
        
        else :
            temp[i] = temp[i - 1]
    
    ar[c] = temp

fi('a')
fi('b')
fi('c')
fi('d')
fi('e')
fi('f')
fi('g')
fi('h')
fi('i')
fi('j')
fi('k')
fi('l')
fi('n')
fi('m')
fi('o')
fi('p')
fi('q')
fi('r')
fi('s')
fi('t')
fi('u')
fi('v')
fi('w')
fi('x')
fi('y')
fi('z')

for i in range(q) :
    a, l, r = input().split()
    l = int(l); r = int(r)

    print(ar[a][r + 1] - ar[a][l])