#!/usr/local/bin/python3

#########################################################################################################
# Maximum and Minimum Loops                                                                            #
#########################################################################################################

# finding largest value in the list

largest = None
print('Before:', largest)

for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)
print('\nLargest:', largest)

# finding smallest value in list sequence
smallest = None
print('\nBefore:', smallest)

for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop: ', itervar, smallest)
print('\nSamllest: ',smallest)

# using max() and min() functions
list = [3, 41, 12, 9, 74, 15]
max_value = max(list)
min_value = min(list)
print("\nMaximum value:", max_value, "\nMinimum value:", min_value)

# built-in min() function 
values = [3, 41, 12, 9, 74, 15]

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
print('\nSmallest value:',min(values))        

# built-in max() function 
def max(values):
    largest = None
    for value in values:
        if largest is None or value > largest:
            largest = value
    return largest
print('\nLargest value:',max(values))   