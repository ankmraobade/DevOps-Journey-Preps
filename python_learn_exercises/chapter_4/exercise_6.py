#!/usr/local/bin/python3

#########################################################################################################################
# Task:	Rewrite your pay computation with time-and-a-half for over-time and create a function called 			#
#	computepay which takes two parameters(hours and rate).						 		#
#########################################################################################################################

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

def computepay(x,y):
    if ( hours <= 40 ):
     pay = hours * rate
     print("Pay: ", pay)
    
    else:
     pay = hours * rate
     extra_hours_worked  = hours - 40
     extra_pay = 0.5 * rate * extra_hours_worked

     print("Pay: ", pay + extra_pay)

computepay(hours,rate)

