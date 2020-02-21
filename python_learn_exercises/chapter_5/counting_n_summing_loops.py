#!/usr/local/bin/python3

#########################################################################################################
# Counting and Summing Loops                                                                            #
#########################################################################################################

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count of list:',count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Summing - Total:',total)


list_str = ['a','b','c','d']
count_str = len(list_str)
print('Count of strings:', count_str)

list_int = [10, 12, 14, 15, 16, 20]
count_int = len(list_int)
print('Count of Integers:', count_int)

