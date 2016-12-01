list = [2,3,5,7,9,13]

def binary_search(list, low, high):
    L = len(list)
    r = list[round(L/2)]
    if L == 1 and r < low or r > high+1:
        return False
    elif r >= low and r <= high:
        return True
    elif low > r:
        return binary_search(list[round(L/2)::1],low,high)
    elif high+1 < r:
        return binary_search(list[:round(L/2):1],low,high)
    else:
        return False

low = int(input('Please enter low end of range: '))
high = int(input('Please enter high end of range: '))
print('{}'.format(binary_search(list,low,high)))


