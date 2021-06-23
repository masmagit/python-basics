# Working with Lists, indexing starts with 0

def basic_lists():
    fruits = ["orange", "apple", "banana", "mango"]

    # fruits[-1]  # Last item in the list, negative indexing means beginning from the end
    # fruits[1:3]  # Returns 2nd and 3rd elements 
    # fruits[2] = "pear"  # Change 3rd element 

    # print("apple" in fruits)  # Use in to check

    # for i in fruits:  # Loop through
    #    print(i)

    # fruits.append("avo")  # Add an element at the end
    # fruits.insert(2, "avo")

    # fruits.remove("orange")  # Remove an element
    # e = fruits.pop(2)        # Remove an element at index
    # del fruits[1:3]  # Remove slice in the list. del can be used to delete a variable    

    # fruits.sort()  # Sort the list

    # fruits.clear()  #Clear the list      
    # f = fruits.copy()  # Copy the list
# basic_lists()

# Assigning list values to multiple variables
# my_list = [1, 2, 3, 4, 5, 6]
# a, *b, c = my_list
# a = 1, b = [2, 3, 4, 5], c = 6

# A List Comprehension consists of brackets containing an expression followed by a for clause, 
#   then zero or more for or if clauses
# squares = [x**2 for x in range(10) if not (x in [2,5])]
# print(squares)

def build_sets():
    print(build_sets.__name__)
    
    sets_co = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    
    # is equal to:
    
    sets = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x != y:
                sets.append((x, y))
    
    print(sets_co)
    print(sets)

    # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# build_sets()

def nested_list_exp():
    print(nested_list_exp.__name__)
    
    nestedlist = [
        [0,1,2], 
        [3,4,5]
    ]
    return([[row[i] for row in nestedlist] for i in range(2)])
print(nested_list_exp())    # [[0, 3], [1, 4]]

# is equal to:

def nested_list_loop():
    print(nested_list_loop.__name__)
    
    nestedlist = [
        [0,1,2], 
        [3,4,5]
    ]
    newlist = []
    for i in range(2):
        listrow = []
        for row in nestedlist:
            listrow.append(row[i])
        newlist.append(listrow)
    return(newlist)
print(nested_list_loop())   # [[0, 3], [1, 4]]

if __name__ == "__main__":
    build_sets()