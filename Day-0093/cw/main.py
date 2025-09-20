from functools import reduce

a = lambda num: num % 2

set = {2, 3, "hello", (1, 2, 3), True, 1}

print(set)

me = {
    "name": "irakli",
    "lastname": "ugulava",
    "age": 16
}

nums = [1,2,3,4,5]
sqr = list(map(lambda x: x ** 2, nums))
print(sqr)

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

prod  = reduce(lambda x, y: x * y, nums)


numbers = [5, 12, 18, 7, 25]
even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

numbers = [4, 7, 10, 13, 15, 18, 21, 24, 27, 30]
odd = list(filter(lambda x: x % 2 != 0, numbers))

print(odd)

numbers = [4, 7, 10, 13, 15, 18, 21, 24, 27, 30]
add = reduce(lambda x, y: x + y, numbers)

numbers = [4, 7, 10, 13, 15, 18, 21, 24, 27, 30]
updated = list(map(lambda x: x + 10, numbers))
print(updated)
