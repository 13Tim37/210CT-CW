n = int(input('Enter an integer: '))

def checkPrime(n, x):
    if n < 2:
        return False
    if x == 1:
        return True
    else:
        if n % x == 0:
            return False
        else:
            return checkPrime(n, x - 1)

print(checkPrime(n, n-1))
