#!/usr/local/bin/python3

#########################################################################
# Example of 4.9 section from the book					#
#########################################################################

import math			# importing math module

def print_twice(bruce):		# function header or definition
    print(bruce)		# function body ..... 
    print(bruce)

print_twice('Spam')		# calling function and passing the argument 'Spam' to replace 'bruce'

print_twice(17)			# calling function and passing the argument '17' to replace 'bruce'

print_twice(math.pi)		# calling math.pi() function from math module to evaluate the value, then print_twice()

print_twice('Spam ' * 4)	# evaluating the arugment, then calls the function with result of an argument

print_twice(math.cos(math.pi))	# evaluating the arugment, then calls the function with result of an argument

michael = 'Eric, the half a bee.'	# using a variable
print_twice(michael)			# variable as an argument







