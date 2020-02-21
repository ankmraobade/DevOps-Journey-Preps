#!/usr/local/bin/python3

#########################################################################################################################
# Task:	Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 	#
#	and print out the converted temperature.									#
#															#
#########################################################################################################################

celsius = float(input("Enter the temperature in Celsius:"))
fahrenheit = celsius * 9/5 + 32

print ("Fahrenheit value: ",fahrenheit)


# Additionally converting Fahrenheit to Celsius

fahrenheit = float(input("Enter the temperature in Fahrenheit:"))
celsius = (fahrenheit-32) * 5/9

print ("Celsius value:",celsius)


