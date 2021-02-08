""" 
My fizzbuzz solution

Author: Jordan R. Hall, Date: 12/16/2020

Main feature: script which prints (on a new line) every integer from 1 to 100
              but replacing all factors of 3 with 'fizz,' factors of 5 with 'buzz', and
              factors of both with 'fizzbuzz'
"""

stop = int(1E2)
factors = [3, 5]
strings = ['fizz', 'buzz']

def FactorChecker(number:int, factor:int, message:str) -> str:
    if number % factor == 0: return message
    else: return ''

my_string = ''

for i in range(1, stop + 1):
    temp_string = ''
    for factor, message in zip(factors, strings):
        temp_string += FactorChecker(i, factor, message)
    
    if len(temp_string) == 0: temp_string = str(i)
        
    
    my_string += temp_string + '\n'
        
print(my_string)
