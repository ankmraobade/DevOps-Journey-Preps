#!/usr/local/bin/python3
# coding=utf8
###########################################################################################################
# Task: Write a program which repeatedly reads numbers until the user enters �done�. Once �done� is       #
#       entered, print out the total, count, and average of the numbers. If the user enters anything      #
#       other than a number, detect their mistake using try and except and print an error message and     # 
#       skip to the next number.                                                                          #
#                                                                                                         #
#    Enter a number: 4                                                                                    #
#    Enter a number: 5                                                                                    #
#    Enter a number: bad data                                                                             #
#    Invalid input                                                                                        #
#    Enter a number: 7                                                                                    #
#    Enter a number: done                                                                                 #
#    16 3 5.333333333333333     [5+4+7   16/3]                                                            #
###########################################################################################################

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
    except:
        print(error_msg)
if count!=0:
    avg = total / count
    print('\nTotal: ', total)
    print('Count: ', count)
    print('Average: ', avg)

# function for same 
def exercise1():
    total = 0
    count = 0
    while True:
        number = input('Enter a number:')
        if number == 'done':
            print('\n',total, count, (total / count))
            break
        else:
            try:
                total = total + float(number)
            except:
                print('Invalid input')
                continue
            count = count + 1

exercise1()
