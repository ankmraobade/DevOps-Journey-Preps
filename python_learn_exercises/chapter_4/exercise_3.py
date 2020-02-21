#!/usr/local/bin/python3

#########################################################################################################################
# Task:	Move the function call back to the bottom and move the definition of print_lyrics after the definition 		#
#	of repeat_lyrics. What happens when you run this program?							#
#########################################################################################################################

#repeat_lyrics()			# Moved to end

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():			# moved this function next to repeat_lyrics()
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()				# function call 


