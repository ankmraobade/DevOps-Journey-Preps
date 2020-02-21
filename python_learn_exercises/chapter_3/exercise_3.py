#!/usr/local/bin/python3

#########################################################################################################################
# Chapter 3 : Exercise Number - 3											#
#															#
# Task:	Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error 	#
#	message. If the score is between 0.0 and 1.0, print a grade using the following table:				#
#															#
#	Score 		Grade												#
#	>= 0.9 		A												#
#	>= 0.8 		B												#
#	>= 0.7 		C												#
#	>= 0.6 		D												#
#	< 0.6 		F												#
#########################################################################################################################

error_msg = "Bad score"

try:

 score = float(input("Enter the score between 0.0 to 1.0 : "))
 if ( score >= 0.0 and score <= 1.0 ):
  if ( score >= 0.9 ):
   print("A")
  elif ( score >= 0.8 ):
   print("B")
  elif ( score >= 0.7 ):
   print("C")
  elif ( score >= 0.6 ):
   print("D")
  elif ( score < 0.6 ):
   print("F")
 else:
  print(error_msg)
except:
 print(error_msg)
 
