num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 < num2:
    print(f"{num1} is the smaller number")
elif num2 < num1:
    print(f"{num2} is the smaller number")
else:
    print("Both numbers are equal:")
    