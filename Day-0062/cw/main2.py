def find_different_elements(arr1, arr2):
    result = []
    for item in arr1:
        if item not in arr2:
            result.append(item)
    for item in arr2:
        if item not in arr1:
            result.append(item)
    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
result = find_different_elements(arr1, arr2)
print(result)
