num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Square s")

operation = input("Enter operation number (1-5): ")

if operation == "1":
    result = num1 + num2
    print("Result: ", result)
elif operation == "2":
    result = num1 - num2
    print("Result: ", result)
elif operation == "3":
    result = num1 * num2
    print("Result: ", result)
elif operation == "4":
    result = num1 / num2
    print("Result: ", result)
elif operation == "5":
    print("Square of num1:", num1**2)
    print("Square of num2:", num2**2)
else:
    print("Invalid operation number")