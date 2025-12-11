def count_multiples(arr):
    result = {}
    # for every element if it is divisible by numbers from 1-9 then add count to that number
    for i in range(1, 10):
        count = 0
        for x in arr:
            if x % i == 0:
                count += 1
        result[i] = count

    return result

arr = []
n = int(input("Enter limit of the array"))
for i in range(n):
    arr[i]= int(input("Enter the numbers"))
print(count_multiples(arr))