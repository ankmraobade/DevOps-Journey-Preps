#!/usr/local/bin/python3

##########################################################################################################
# Task:	Rewrite the grade program from the previous chapter using a function called computegrade that    #
#	takes a score as its parameter and returns a grade as a string. 						             #
#															                                             #
#	Score 	Grade												 	                                     #
#	>= 0.9 	A													                                         #
#	>= 0.8 	B													                                         #
#	>= 0.7 	C													                                         #
#	>= 0.6 	D													                                         #
#	< 0.6 	F													                                         #
##########################################################################################################

error_msg = "Bad score"

score = float(input("Enter the score between 0.0 to 1.0 : "))

def computegrade(x):
    try:
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

computegrade(score)
