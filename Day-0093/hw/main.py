x = lambda name: print(f"hello {name}")
x("irakli")

num = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, num))
print(doubled)


nums = [1, 3, 5, 6, 7, 10, 15, 21, 25.5, 30, 101, 105]
filtered = list(filter(lambda x: x % 5 == 0, nums))
print(filtered)


# შექმენით Set მოცემული მნიშვნელობებით:
# setn = {"Goa", "Novatori", "Stem", 123, True, 1, False, 0}

# და ახსენით რატომ არ გამოვა 0 და 1 
# radgan True = 1 da False = 0, da set-shi ar shegvilia ori ertnairi mnishvnelobis shenaxva 1 da 0 ar sheinaxeba