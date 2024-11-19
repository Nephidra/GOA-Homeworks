nums = [1, 2, 3, 4, 5]
nums_copy = []
nums_2 = [11, 12, 13, 15]
counter = 0
i = 0
i_2 = 0
i_3 = 0
i_4 = 0
i_5 = 0
reverse = []

nums.append(6)
nums.append(7)
nums.append(8)
nums.append(9)
nums.append(10)

nums_copy = nums.copy()
counter = nums.count(9)

nums_copy.extend(nums_2)

i = nums_copy.index(2)
i_2 = nums_copy.index(3)
i_3 = nums_copy.index(4)
i_4 = nums_copy.index(5)
i_5 = nums_copy.index(6)

nums_copy.insert(13, 14)
nums_copy.insert(2, 5)
nums_copy.insert(7, 9)
nums_copy.insert(10, 1)
nums_copy.insert(11, 3)

nums_copy.pop(14)
nums_copy.pop(3)
nums_copy.pop(6)
nums_copy.pop(9)
nums_copy.pop(11)

nums_copy.remove(14)
nums_copy.remove(1)
nums_copy.remove(7)
nums_copy.remove(6)
nums_copy.remove(11)

nums_copy.reverse()

nums_copy.clear()