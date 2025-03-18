'''
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) 
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    '''
def find_and_replace(lst, find_val, replace_val):
    #check if the input is a list if not return -1
    if not type(lst)== list:
        return -1
    #looping through the find_value list and check
    for counter in range(len(lst)):
        # if the current element matches find_val replace with replace_val
        if lst[counter] == find_val:
            lst[counter] = replace_val
    # after replace return the list
    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)) 
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange")) 