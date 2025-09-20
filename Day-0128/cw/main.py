def min_min_max(arr):
    value1 = min(arr)
    value2 = max(arr)
    value3 = set(arr)
    
    min_absent = None
    for i in range(value1, value2 +1) :
        if i not in value3 :
            min_absent = i
            break
    if min_absent is None :
        min_amsent = value2
    return [value1, min_absent, value2]



def invite_more_women(arr):
    man = arr.count(1)
    woman = arr.count(-1)
    return woman < man