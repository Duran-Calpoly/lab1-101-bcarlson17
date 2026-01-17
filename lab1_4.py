def calculate_average	(num1, num2, num3):
  avg = num1 + num2 + num3
  avg /= 3
  return avg

def add_tax	(bill_total):
  tax = bill_total / 10
  tax = bill_total + tax
  return tax

def greet_user (name):
  return "Hello " + name
calculate_average	(1, 2, 3)
add_tax	(50)
greet_user (input ("Whats your name?"))