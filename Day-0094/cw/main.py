nums = [1, 3, 5, 6, 7, 12, 15, 21, 25.5, 30, 101, 105]
filtered = list(filter(lambda x: x % 12 == 0, nums))
print(filtered)

