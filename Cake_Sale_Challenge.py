# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:29:30 2021

@author: carte
"""

#Cake Sale Challenge


#Step 1: Input
cupcakes = int(input("How many cupcakes do you plan to sell? "))
macaron = int(input("How many macarons do you plan to sell? "))
cheesecake = int(input("How many cheesecakes do you plan to sell? "))
cupcakePrice = float(0.40)
macaronPrice = float(0.50)
cheesecakePrice = float(0.70)

#Step 2: Process
cupcakeTotal = cupcakes * cupcakePrice
macaronTotal = macaron * macaronPrice
cheesecakeTotal = cheesecake * cheesecakePrice

#total of all the cupcake income, float used for decimals
total = float(cupcakeTotal + macaronTotal + cheesecakeTotal)

#Use to format the number to have 2 decimal points when executed
formatted_total = format(total, ".2f")

#End Result
print("You made: $", formatted_total)


