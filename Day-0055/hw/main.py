num1 = float(input("a="))
num2 = float(input("b="))

operation = input("ჩაწერეთ ოპერაცია (+ ან -): ")

if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
else:
    print("არასწორი ოპერაცია! შეარჩიეთ + ან -.")