# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:46:47 2021

@author: carte
"""




# importing numpy package w/ variable np
import numpy as np

# Setting the variables
low = 100
high = 5000
rand_num = np.random.randint(low,high)

user_guess = 0
# Setting the "Big Picture"
while user_guess != rand_num:
# the intro/ user input 
    my_string = 'Guess the integer between ' + str(low) + ' and ' + str(high) + '  :  '
    user_guess = input(my_string)
# making sure that the value is an number
    if isinstance(user_guess,(int,float,complex)) == ValueError:
        print('Do you even know what numbers are?')
        user_guess = 0
 # casting input as an integer; required for ifs and elifs  
    user_guess = int(user_guess)

    if user_guess == 0:
        print('Try again')
#parameter for when the input equals the random number
    elif user_guess == rand_num:
        print('You Guessed It!')
# if input is higher than the random number, but within the range
    elif user_guess > rand_num and user_guess <= high:
        print('You are too high!')
# if input is lower than the random number, but within the range
    elif user_guess < rand_num and user_guess != 0 and user_guess >= low:
        print('You are too low!')
# if input is below the minimum range
    elif user_guess < low and user_guess != 0:
        print('You are below the minimum!')
# if input is above the maximum range
    elif user_guess > high:
        print('You are higher than the maximum!')
    