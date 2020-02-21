#!/usr/local/bin/python3

#########################################################################
# 4.11 section: calling functions from other script			#
#########################################################################

from simple_math_functions import addition, subtraction, multiplication, division

# print(addition(3,5))			# without storing result
add_result = addition(3,5)		# storing result in a variable
sub_result = subtraction(3,5)
mul_result = multiplication(3,5)
div_result = division(3,5)

print("Addition: ", add_result)
print("Subtaction: ", sub_result)
print("Multiplication: ", mul_result)
print("Division: ", div_result)
