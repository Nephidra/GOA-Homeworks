def two_sum(nums, target):
    num_to_index = {}
    
    for index in range(len(nums)):
        num = nums[index]
        difference = target - num
        
        if difference in num_to_index:
            return [num_to_index[difference], index]
        
        num_to_index[num] = index
    
    return None