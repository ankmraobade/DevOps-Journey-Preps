#!/usr/local/bin/python3

#########################################################################################################
# Updating variables                                                                                    #
#########################################################################################################

x = 0           # initializing variable 'x'
y = 1           # initializing variable 'y'

x = x + y       # Evaluates the value in the right side then assign it to variable 'x'
print(x)

x = x + 1       # increment done by updating variable
print(x)

x = z + 1       # variable 'z' is not initialized before evaluation - throws NameError
print(x)
