'''
Task 1
- Create a function that finds the first negative number in a list (lst).
- Return the first negative number if found, otherwise return "No negatives".
- Use a while loop to implement this.
'''

def find_first_negative(lst):
    count = 0 # generic counter

    while count <len(lst): # looping list through counter
        if lst[count] < 0: # if there is a negative number then return it 
            return lst[count]  
        count +=1 # move the index to next
    #else return no negatives      
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))