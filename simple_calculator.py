from ast import operator


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1 for ADDITION")
print("2 for SUBSTRACTION")
print("3 for MULTIPLICATION")
print("4 for DIVISION")
print("5 for FLOOR DIVISION")
print("6 for REMAINDER")
print("7 for EXPOENTIAL")

operator = int(input("Enter the operator: "))

if (operator == 1):
    value = num1 + num2
    print(f"The value of {num1} + {num2} = {value}")
elif (operator == 2):
    value = num1 - num2
    print(f"The value of {num1} - {num2} = {value}")
elif (operator == 3):
    value = num1 * num2
    print(f"The value of {num1} * {num2} = {value}")
elif (operator == 4):
    value = num1 / num2
    print(f"The value of {num1} / {num2} = {value}")
elif (operator == 5):
    value = num1 // num2
    print(f"The value of {num1} // {num2} = {value}")
elif (operator == 6):
    value = num1 % num2
    print(f"The value of {num1} % {num2} = {value}")
elif (operator == 7):
    value = num1 ** num2
    print(f"The value of {num1} ^ {num2} = {value}")
else:
    print("Enter proper input")
