def series(x):
    res =[]
    #for every number we are multiplying by 2 and decreasing 1 from it
    for i in range(1,x+1):
        res.append((i*2)-1)

    return res

x = int(input("Enter Number"))
print(series(x))