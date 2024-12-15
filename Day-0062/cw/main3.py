def remove_elements(arr1, arr2):
    result = []
    for item in arr1:
        if item not in arr2:
            result.append(item)
    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 5]
result = remove_elements(arr1, arr2)
print(result)
