'''
Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
'''

def swap(x, y):    
    # check if the number is int or flot for both x and y             
    if not (type(x) == int) or ((type(x) == float) and (type(y) == int)) or (type(y) == float):
        # if the condition is met it will send -1 
        return -1
    #swapping the variables x and y
    x,y = y, x
    #printing the variables after swap
    print(x, y)

#Task 2
#Invoke the function "swap" using the following scenarios:
#- "Apple", 10
#- 9, 17
    
print(swap("Apple", 10)) # uses print to display the returned value
swap(9,7)