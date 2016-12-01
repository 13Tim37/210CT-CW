from math import floor

def perfectNumber(x):
    # To find the closest square number for x: sqrt and floor.
    n = floor(x**0.5)
    return n

p = int(input('Please enter a positive integer: '))

j = perfectNumber(p)
print('Smallest perfect squre is {} x {}'.format(j,j))

#PERFECT-NUMBER(A)
#    n = floor(A)
