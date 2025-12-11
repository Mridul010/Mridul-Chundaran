def series(x):
    res =[]
    for i in range(1,x+1):
        res.append((i*2)-1)

    return res

x = int(input("Enter Number"))
print(series(x))