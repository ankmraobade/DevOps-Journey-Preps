#!/usr/local/bin/python3

#########################################################################
# Example of 4.10 section from the book					#
#########################################################################

# void function: don't have a return value.

def addition(a,b):		# function without return value
    add = a + b
    
x = addition(3,5)		# calling function with arguments 
print(x)			# special value "None" gets printed, from 'NoneType'

