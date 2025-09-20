def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive_count = 0
    negative_sum = 0
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num
    return [positive_count, negative_sum]