'''
Task 1
- Create a function to check if the number (num) is divisible by another number (divisor).
- Both num and divisor must be numeric.
- Return True if num is divisible by divisor, False otherwise.
'''

def check_divisibility(num, divisor):

    if not (type(num) == int) or ((type(num) == float) and (type(divisor) == int)) or (type(divisor) == float):
        return -1
    
    # check if divisor is 0
    if divisor == 0:
        return "Error: Division by zero is undefined."

    if num % divisor == 0:
        return True
    else:
        return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(-10,2))
print(check_divisibility(-7,3))
