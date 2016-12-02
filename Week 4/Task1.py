list = [2,3,5,7,9,13]

def binary_search(list, low, high):
    L = len(list)
    #print('INDEX: ' + str(int(((L/2)+0.5)//1)))
    #print('LIST: ' + str(list))
    if L == 1:
        index = 0
    else:
        # Have to use this to round as python round function uses 'bankers rounding'
        index = int(((L/2)+0.5)//1)
    r = list[index]
    #print('LOW: ' + str(low) + ', HIGH: ' + str(high))
    #print('L: ' + str(L))
    #print('r: ' + str(r))
    #print('-----------')
    if L == 1 and (r < low or r > high+1):
        return False
    elif r >= low and r <= high:
        return True
    elif low > r:
        return binary_search(list[index::1],low,high)
    elif high < r:
        return binary_search(list[:index:1],low,high)
    else:
        return False

low = int(input('Please enter low end of range: '))
high = int(input('Please enter high end of range: '))
print('{}'.format(binary_search(list,low,high)))


