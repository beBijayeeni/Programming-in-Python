def AlternativePrint(arr):
    arr2 = sorted(arr)
    print(arr2)
    result = []
    for i in range(0,len(arr2),2):
        result.append(arr2[i])
    return result
arr = [5,5,8,2,6,7]
result = AlternativePrint(arr)
print(result)
