def series(x):
    res = []
    for i in range(1,x+1):
        if i == 1:
            res.append(1)
        elif i%2 ==0:
            continue
        else:
            res.append(((i-1)*2)-1)
            res.append((i*2)-1)
    return res

x = int(input("Enter the range"))
print(series(x))