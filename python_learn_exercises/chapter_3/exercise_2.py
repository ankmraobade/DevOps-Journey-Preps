#!/usr/local/bin/python3

#########################################################################################################################
# Chapter 3 : Exercise Number - 2											#
#															#
# Task: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by 	#
# 	printing a message and exiting the program. The following shows two executions of the program:			#
#															#
#	Enter Hours: 20													#
#	Enter Rate: nine												#
#	Error, please enter numeric input										#
#															#
#	Enter Hours: forty												#
#	Error, please enter numeric input										#
#########################################################################################################################

exception_msg = "Please enter numeric value"

name = str(input("Empoyee name:"))

try:
 hours = int(input("Number of hours worked:"))
 rate = float(input("Pay rate:"))
 pay = hours * rate
 if (hours > 40):
  extra_hours_worked = hours - 40
  extra_pay = 0.5 * rate * extra_hours_worked
  total_pay = pay + extra_pay
  print("Increased pay:",extra_pay) 
  print("Hello", name," - your total pay is:",total_pay)
 else:
  print(name," - Your pay is:",pay)

except:
 print(exception_msg)

 
