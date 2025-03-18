'''
Task 1
- Create a function that reverses a given string (s).
- s must be a string.
- Return the reversed string.
'''
def string_reverse(s):

    return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

txt = string_reverse("Hello World")
print(txt)
txt2 = string_reverse("Python")
print(txt2)