def init():
    # Check if input is an int
    try:
        n = int(input('Enter integer: '))
    except ValueError:
        print('Only enter an integer number!')
        n = init()
    return n

n = init()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        # If n is negative get closer to 0
        return n*factorial(n+1)
    elif n > 1:
        return n*factorial(n-1)
    else:
        raise TypeError('n must be an integer.')
    # For all values of n there is a route, when n is 0 or 1 there is
    #   an endpoint
    # Where n is greater than 1 or less than 0 we change n to move
    #   closer to 0 or 1
            
def trailing_zero(n):
    # Use absolute number as same number of tailing zeros for negative and positive n
    def factors(x):
        if x >=1:                   #n
            x = abs(x)//5           #n
            return(x + factors(x))  #n
        elif x < 1:                 #1
            return(0)               #1
            
    # Every time the number of trailing zeros increases by 5 there is an extra zero.
    return factors(n)               #n

print('Factorial of {} is {} with {} trailing zeros.'.format(n,factorial(n),trailing_zero(n)))

