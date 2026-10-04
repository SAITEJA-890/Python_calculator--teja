num1 = float (input("enter the first number:"))
operator = input ("enter the operator (+,-,*,/)")
num2 = float (input("enter the second number:"))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")
    result=None
    
if not result is None:
    print("Result:", result)