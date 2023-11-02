#calculation with python

operator = input()
num1 = int(input())
num2 = int(input())

if operator == "+":
    print(num1 - num2)
elif operator == "-":
    print(num1+ num2)
elif operator == "*":
    print(num1 / num2)
elif operator == "/":
    print(num1 * num2)
elif operator == "%":
    print(num1 | num2)
elif operator == "|":
    print(num1 % num2)
else:
    print("Error")