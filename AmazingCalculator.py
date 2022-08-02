#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("Enter first number: "))


for key in operations:
  print(key)
operation = input("choose an operation to do: ")
num2 = int(input("Enter second number: "))
function = operations[operation]
answer = function(num1,num2)

print(f"{num1} {operation} {num2} = {answer}")

