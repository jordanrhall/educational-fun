# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:29:30 2021

@author: carte
"""

#Cake Sale Challenge

cupcakePrice = float(0.40)
macaronPrice = float(0.50)
cheesecakePrice = float(0.70)

#Step 1: Input
cupcakes = int(input("How many cupcakes do you plan to sell? "))
macaron = int(input("How many macarons do you plan to sell? "))
cheesecake = int(input("How many cheesecakes do you plan to sell? "))

#Step 2: Process
cupcakeTotal = cupcakes * cupcakePrice
macaronTotal = macaron * macaronPrice
cheesecakeTotal = cheesecake * cheesecakePrice

Total = float(cupcakeTotal + macaronTotal + cheesecakeTotal)

#End Result
print(Total)