# Program make a simple calculator

#  adds two numbers
def add(x, y):
    return x + y

#  subtracts two numbers
def subtract(x, y):
    return x - y

#  multiplies two numbers
def multiply(x, y):
    return x * y

#  divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))