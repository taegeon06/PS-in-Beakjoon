a, b, c, d, e, f = map(float, input().split())

if (a != 0) :
    Y = (f - d * c / a) / (e - d * b / a)
    X = (c - b * Y) / a

elif (b != 0) :
    X = (f - e * c / b) / (d - e * a / b)
    Y = (c - a * X) / b
    
elif (d != 0):
    Y = (c - a * f / d) / (b - a * e / d)
    X = (f - e * Y) / d

elif (e != 0) :
    X = (c - b * f / e) / (a - b * d / e)
    Y = (f - d * X) / e

print(round(X), round(Y))