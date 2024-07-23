# def even_sum() :
#     nums = [1, 2, 3, 4, 5]
#     even_sum = 0
#     for i in range(5) :
#         if nums[i] % 2 == 0 :
#             even_sum += nums[i]
#     return even_sum
# print(even_sum())

# def reverse() :
#     word = "GOA"
#     i = len(word) - 1
#     while i >= 0 :
#         print(word[i])
#         i -= 1
# reverse()

# def factorial_(a) :
#     factoria = 1
#     i = 1
#     while i <= a :
#         factoria *= i
#         i+= 1
#     return factoria
# print(factorial_(5))

# def common() :
#     list_1 = [1, 2, 3, 4, 5]
#     list_2 = [3, 4, 5, 6, 7]
#     list_3 = []
#     for i in range(5) :
#         for l in range(5) :
#             if list_1[i] == list_2[l] :
#                 list_3.append(list_1[i])
#     return list_3
# print(common())

# def vowels() :
#     a = "GOA"
#     b = []
#     for i in range(3) :
#         if a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U" :
#             b.append(a[i])
#     return b
# print(vowels())

# def sorting() :
#     l1 = [2, 1, 7, 6, 9]
#     for i in range(0, len(l1)):
#         for l in range(i+1, len(l1)):
#             if l1[i] >= l1[l]:
#                 l1[i], l1[l] = l1[l],l1[i]

#     print(l1)
# sorting()

# def perm() :
#     w1 = "ABC"
#     w2 = "BCA"
#     list_1 = list(w1)
#     list_2 = list(w2)
#     list_1.sort()
#     list_2.sort()
#     print(list_1 == list_2)
# perm()

# def transp() :
#     matrix = [[1, 2], [3, 4], [5, 6]]
#     for row in matrix:
#         print(row)
#     rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
#     print("\n")
#     for row in rez:
#         print(row)
# transp()

# def prime():
#     num = 12
#     if num > 1:
#         for i in range(2, (num//2)+1):
#             if (num % i) == 0:
#                 print("False")
#                 break
#         else:
#             print("True")
#     else:
#         print("False")
# prime()

# def sorting_words() :
#     l1 = ["Ae", "Bae", "Zeea", "Goa", "Amga"]
#     for i in range(0, len(l1)):
#         for l in range(i+1, len(l1)):
#             if len(l1[i]) >= len(l1[l]):
#                 (l1[i]), (l1[l]) = (l1[l]), (l1[i])

#     print(l1)
# sorting_words()
