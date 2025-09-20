def stray(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num