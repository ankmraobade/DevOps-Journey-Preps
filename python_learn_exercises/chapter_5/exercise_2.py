#!/usr/local/bin/python3
# coding=utf8
###########################################################################################################
# Task:  Write another program that prompts for a list of numbers as above and at the end prints out      #
#        both the maximum and minimum of the numbers instead of the average.                              #
#                                                                                                         #
###########################################################################################################

smallest = None
largest = None
total = 0
count = 0
error_msg = 'Invalid input'

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        if float(number):
            total = total + float(number)
            count = count + 1
            itervar = float(number)
            if largest is None or itervar > largest:
                largest = itervar
            if smallest is None or itervar < smallest:
                smallest = itervar
    except:
        print(error_msg)
if count != 0:
    print('Largest: ', largest, '\nSmallest: ', smallest)