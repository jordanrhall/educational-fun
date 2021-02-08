# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:29:30 2021

@author: carte
"""

#Cake Sale Challenge


#Step 1: Input

#constants in $ unit, no user input required
cupcakePrice = float(0.40)
macaronPrice = float(0.50)
cheesecakePrice = float(0.70)

#we must ensure that our entries are valid

while True:    
#check cupcake input, if it's not a whole number, gives message and restarts current loop  
    try:       
        cupcakes = int(input("How many cupcakes do you plan to sell? "))
    except ValueError:
        print('Please ensure your entry contains only numbers. No letters or special characters.')
        continue
    else:
        break
    
while True:
#check macaron input, if it's not a whole number, gives message and restarts current loop    
    try:
        macaron = int(input("How many macarons do you plan to sell? "))
    except ValueError:
        print('Please ensure your entry contains only numbers. No letters or special characters.')
        continue
    else:
        break

while True:
#check cheesecake input, if it's not a whole number, gives message and restarts current loop      
    try:       
        cheesecake = int(input("How many cheesecakes do you plan to sell? "))
    except ValueError:
        print('Please ensure your entry contains only numbers. No letters or special characters.')
        continue
    else:
        break
#Step 2: Process 
#multiply number of sold pastries by their respective price for total earned on each  
cupcakeTotal = cupcakes * cupcakePrice
macaronTotal = macaron * macaronPrice
cheesecakeTotal = cheesecake * cheesecakePrice

#total of all the cupcake income, float used for decimals
total = float(cupcakeTotal + macaronTotal + cheesecakeTotal)

#Use to format the number to have 2 decimal points when executed
formatted_total = format(total, ".2f")

#End Result
print("You made: $", formatted_total)


