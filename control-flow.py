
# imitation of  SWITCH() using elif 
# logical operators: and, or, not
# switch(a)
#   case(0)  
#   case(1) 
#   case(2) 
#   else ...
a = 1
if a == 0: 
    print('zero')
elif a == 1:
    print('one')
elif a == 2:
    print('two')
else:
    print('not 0, not 1, not 2')

# WHILE usual
i = 10
while i < 15: 
    print(i)
    i += 1

# FOR usual, RANGE()
#range(5, 10)   #5, 6, 7, 8, 9
#range(0, 10, 3)    #0, 3, 6, 9
#sum(range(4))  # 0 + 1 + 2 + 3
for i in range(5):
    print(i)

# FOR statement iterates over the items of any sequence (a list or a string or collections), 
# in the order that they appear in the sequence
words = ['one', 'five', 'eleven']
for w in words:
    print(w, len(w))  # one 3 five 4 eleven 6

# The BREAK statement, like in C, breaks out of the innermost enclosing for or while loop. 
# LOOP statements may have an ELSE clause; 
#   it is executed when the loop terminates through exhaustion of the iterable (with for) 
#   or when the condition becomes false (with while)  
# The CONTINUE statement, also borrowed from C, continues with the next iteration of the loop
for i in range(2, 5):
    if i == 3:
        print(i)
        continue
    print(f"{i} is not three")

# The PASS statement does nothing. 
# It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# Comparisons can be chained. 
# For example, a < b == c tests whether a is less than b and moreover b equals c.