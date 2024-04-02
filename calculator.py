def calculate(num1, operator, num2):
  """Performs the specified mathematical operation."""
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Division by zero"
    else:
      return num1 / num2
  else:
    return "Error: Invalid operator"

def get_number(prompt):
  """Gets a valid number input from the user."""
  while True:
    try:
      number = float(input(prompt))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operator():
  """Gets a valid operator input from the user."""
  while True:
    operator = input("Enter an operator (+, -, *, /): ")
    if operator in "+-*/":
      return operator
    else:
      print("Invalid operator. Please enter +, -, *, or /.")

def main():
  """Runs the calculator program."""
  print("Welcome to the Attractive (Text-Based) Calculator!")
  while True:
    num1 = get_number("Enter the first number: ")
    operator = get_operator()
    num2 = get_number("Enter the second number: ")

    result = calculate(num1, operator, num2)

    print(f"{num1} {operator} {num2} = {result}")

    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
      break

  print("Thank you for using the calculator!")

if __name__ == "__main__":
  main()
