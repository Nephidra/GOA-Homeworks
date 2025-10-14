# funqcia - array integerebis - target - return index two numbers which sum = to target

# def first(arr, target):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return arr[i], arr[j]
#     return None  

# print(first([2, 7, 11, 15], 9))


# def first(arr, target):
#     s = set()
#     for i in arr:
#         c = target - i
#         if c in s:
#             return c, i
#         s.add(i)
#     return None

# print(first([2, 2, 11, 15], 4))



# def second(s):
#     start = 0
#     maxl = 0
#     maxs = ""
#     seen = {}
#     for i in range(len(s)):
#         char = s[i]
#         if char in seen and seen[char] >= start:
#             start = seen[char] + 1
#         seen[char] = i
#         current = i - start + 1
#         if current > maxl:
#             maxl = current
#             maxs = s[start:i + 1]
#     return maxs






# function - arr - return num - num - len of biggest progession mathematicly

# def third(nums):
#     num_set = set(nums)
#     longest = 0
#     for num in num_set:
#         if num - 1 not in num_set:
#             current = num
#             length = 1
#             while current + 1 in num_set:
#                 current += 1
#                 length += 1
#             longest = max(longest, length)
#     return longest

# print(third([1, 2, 4, 9, 10, 11, 1000, 12]))


# arr strings - 2 type comments : 1 line, multi line 


def fifth(arr) :
    result = []
    current = False
    for line in arr :
        i = 0
        new = ""

        while i < len(line) :
            if not current and i + 1 < len(line) and line[i:i+2] == "/*" :
                current = True
                i += 2
            elif current and i + 1 < len(line) and line[i:i+2] == "*/" :
                current = False
                i += 2
            elif not current and i + 1 < len(line) and line[i:i+2] == "//" :
                break
            elif not current:
                new += line[i]
                i += 1
            else :
                i += 1
        if new :
            result.append(new)
    return result

print(fifth(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
# ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]