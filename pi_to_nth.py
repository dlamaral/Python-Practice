'''
Diogo Amaral 2020
Program that Finds pi tho the nth digit - input by user
'''
import math

def Find_Pi(n_digit):
    '''
    Finds Pi to the nth
    '''
    pi = round(math.pi, n_digit)
    print(pi)

Find_Pi(int(input("Please enter the number of digits (between 1 and 50) for pi you'd like to see: ")))
