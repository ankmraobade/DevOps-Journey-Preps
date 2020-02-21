#!/usr/local/bin/python3

#########################################################################################################################
# Chapter 3 : Exercise Number - 1											#
#															#
# Task:  Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.	#
# Enter Hours: 45													#
# Enter Rate: 10													#
# Pay: 475.0														#
#########################################################################################################################

name = str(input("Empoyee name:"))
hours = int(input("Number of hours worked:"))
rate = float(input("Pay rate:"))
pay = hours * rate

if (hours > 40):
 extra_hours_worked = hours - 40
 extra_pay = 0.5 * rate * extra_hours_worked
 total_pay = pay + extra_pay
 print("Hello", name," - your total pay is:",total_pay)
 print("Increased pay:",extra_pay)
else:
 print(name," - Your pay is:",pay)


 
