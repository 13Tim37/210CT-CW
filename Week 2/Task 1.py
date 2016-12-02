def perfectNumber(i):
    # To find the closest square number for x: sqrt and floor.
    n = int((i**0.5)//1)
    return n

def init():
    try:
        i = int(input('Please enter a positive integer: '))
    except ValueError:
        print('Only enter a positive integer!')
        i = init()
    return i

i = init()

x = perfectNumber(i)
print('Smallest perfect squre is {} x {}'.format(x,x))
