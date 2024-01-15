class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
def main():
    calc = Calculator()

    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = calc.add(num1, num2)
            print("The addition of two Number is = ", result)

        elif choice == '2':
            result = calc.subtract(num1, num2)
            print("The subtraction of two Number is = ", result)

        elif choice == '3':
            result = calc.multiply(num1, num2)
            print("The multiplication of two Number is = ", result)

        elif choice == '4':
            result = calc.divide(num1, num2)
            print("The division of two Number is = ", result)
            
    else:
        print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    main()
