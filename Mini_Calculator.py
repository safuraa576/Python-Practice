print("===== MINI CALCULATOR =====")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

op = input("Enter operation (+, -, *, /, %, **): ")

if op == '+':
    print(a + b)

elif op == '-':
    print(a - b)

elif op == '*':
    print(a * b)

elif op == '/':
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print(a / b)

elif op == '%':
    print(a % b)

elif op == '**':
    print(a ** b)

else:
    print("Invalid operation")