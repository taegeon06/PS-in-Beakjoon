while True :
    li = list(map(int, input().split()))

    if li[0] == 0 and li[1] == 0 :
        break

    print(li[0] * 2 - li[1])