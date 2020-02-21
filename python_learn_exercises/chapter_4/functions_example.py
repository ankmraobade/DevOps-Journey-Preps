#!/usr/local/bin/python3

#########################################################################
# 4.11 section: features of the functions				#
#########################################################################

def addition(a,b):
    add = a + b
    return add

def subtraction(a,b):
    sub = a - b
    return sub

def multiplication(a,b):
    mul = a * b
    return mul

def division(a,b):
    div = a / b
    return div

# print(addition(3,5))			# without storing result
add_result = addition(3,5)		# storing result in a variable
sub_result = subtraction(3,5)
mul_result = multiplication(3,5)
div_result = division(3,5)

print("Addition: ", add_result)
print("Subtaction: ", sub_result)
print("Multiplication: ", mul_result)
print("Division: ", div_result)
