def count_multiples(arr):
    result = {}

    for i in range(1, 10):
        count = 0
        for x in arr:
            if x % i == 0:
                count += 1
        result[i] = count

    return result


arr = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(arr))