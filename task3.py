""" Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом? """

import locale
import math as m

def numberf(number):
    return locale.format('%d', number, grouping=True)

def prime_factors(n): 
    factors = []

    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print(2)
        factors.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(m.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            # print(i)
            factors.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        # print(n)
        factors.append(n)
    
    return factors

# locale.setlocale(locale.LC_ALL, 'en_US')
number = 600_851_475_143
# x = 1
# prime_factor = 1

print(max(prime_factors(number)))