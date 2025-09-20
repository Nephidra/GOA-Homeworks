def is_sorted_and_how(arr):
    ac = 0
    dc = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            ac += 1
        elif arr[i] > arr[i + 1]:
            dc += 1
    
    if ac == len(arr) - 1:
        return "yes, ascending"
    elif dc == len(arr) - 1:
        return "yes, descending"
    else:
        return "no"