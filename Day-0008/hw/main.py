# 2)

num = 5

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False 

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

print("----------- AND -----------")

print(num >= 1 and num <= 10) # True radgan 5 > 1 da 5 < 10
print(num >= 1 and num <= 4) # False radgan 5 > 1 da 5 > 4
print(num > 5 and num <= 10) # False radgan  5 = 5 da meores agar aqvs mnishvneloba
print(num > 5 and num > 10) # False radgan 5 = 5 da meores agar aqvs mnishvneloba

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True radgan 5 > 1 da meores agar aqvs mnishvneloba
print(num >= 1 or num <= 4) # True radgan 5 > 1 da meores agar aqvs mnishvneloba
print(num > 5 or num <= 10) # True 5 = 5 magram meoreshi weria 5 < 10 rac true da anu pirvels mnishvneloba agar aqvs
print(num > 5 or num > 10) # False radgan 5 = 5 da 5 < 10

# 3) 
# and akavshirebs magalitad print(num >= 1 and num <= 10) aq and aris gamoyenebuli anu orive unda iyos true rom
# true dagvibewdos shedegshi 
# or amowmebs ert erti monacemi tu sworia print(num >= 1 or num <= 10) da tu erterti aris swordi mash true mogvcems

# 4)
a = 5
print(a > 1 and a < 10)
print(a > 1 and a < 4)
print(a > 6 and a < 10)
print(a > 2 and a < 7)
print(a > 1 and a < 2)

print(a > 1 or a < 100)
print(a > 6 or a < 10)
print(a == 1 and a < 10)
print(a > 1 and a == 10)
print(a <= 1 and a < 10)

# 5)
x = 7
y = 8
print(7 > 8)
print(7 < 8)
print(7 == 8)
print(7 >= 8)
print(7 <= 8)