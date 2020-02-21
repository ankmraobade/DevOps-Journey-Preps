#!/usr/local/bin/python3

#########################################################################
# Practice of random module and it's functions				#
#########################################################################

import random 		# importing random module to provide access to it's functions

# functin 'randint' take the parameters low and high and returns an 
# integer between low and high (including both)

random_number_pick = random.randint(5,10)				# passing parameters to randint function

print("random integer value [5,10]:",random_number_pick)		# print the random integer number in between


# function 'choice' gives random element from given sequence

elements = [1, 2, 3, 4, 5, 6]

random_choice_pick = random.choice(elements)				# picks random element each time

print("random choice value [1-6]:",random_choice_pick)			# prints picked random element



