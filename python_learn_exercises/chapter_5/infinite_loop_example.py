#!/usr/local/bin/python3

#########################################################################################################
# Infinite loop and break                                                                               #
#########################################################################################################

# Infinite loop 
#n = 10                   # initializing variable

#while True:
#    print(n, end='')
#    n = n - 1
#print('Done!')

# infinite loop with break
# take input from the user until they type done.

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')