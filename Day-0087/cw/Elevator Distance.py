def elevator_distance(array):
    count = 0
    for i in range(1, len(array)) :
        step = abs(array[i] - array[i-1])
        count += step
    return count
    pass