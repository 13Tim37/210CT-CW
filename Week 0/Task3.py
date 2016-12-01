x = float(input("Enter X: "))

def doFunction(x):
    if x < -2:
        return(x**2 + 4*x + 4)
    elif x == 0:
        return 0
    elif x > -2:
        return(x**2 + 5*x)

print("f(x) = {}".format(doFunction(x)))
