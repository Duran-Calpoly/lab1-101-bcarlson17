def check_multiple (number):
    if number % 5 == 0 and number % 3 == 0:
        return True
    else:
        return False
def check_password (input_string):
    if input_string == "Python123":
        return "access granted"
    else:
        return "access denied"
def calculate_federal_tax (salary):
    tax = 0
    if salary <= 11000: 
        tax = 0.1 * salary
    elif salary <= 44725:
        tax = 0.12  * salary
    elif salary <= 95375:
        tax = 0.22 * salary
    elif salary > 95375:
        tax = 0.24 * salary
    return tax


check_multiple (15)

check_password (123)

calculate_federal_tax (12000)