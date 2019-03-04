'''
NAME: main.py
AUTHOR: Roger Aragon
DATE: 3/3/19
DESCRIPTION: celcius to fahrenheit temperature converter
EMAIL: aragonr87056@student.vvc.edu
'''

cel_temp = int(input('Input temperature (in Celcius): '))
fah_temp = (cel_temp * (9 / 5)) + 32

print('The converted temperature is:',fah_temp, 'degrees Fahrenheit.')
