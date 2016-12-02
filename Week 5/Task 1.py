#l = [1,2,3,12,54,7,6,5,22,34,62,123,1234,2,7654]
l = list((input('Please enter a list of integers: ')).split(','))

def mostAscNumbers(l):
    L = []
    start = None
    end = None
    #print('Length: ' + str(len(l)))
    for i in range(0,len(l)):
        j = l[i]
        if len(l) > i+1:
            k = l[i+1]
        else:
            k = l[len(l)-1]
        #print('---------------------')
        #print('I: ' + str(i))
        #print('J: ' + str(j))
        #print('K: ' + str(k))
        if k > j:
            if start == None:
                start = i
                print('Start: ' + str(start))
            continue
        elif k <= j or i == len(l)-1:
            end = i
            print('End: ' + str(end))
            if start != None and (end - start) + 1 > len(L):
                L = l[start:end+1]
                print('L: ' + str(L))
                start = None
    return L

print('Original list: ' + str(l))
print(mostAscNumbers(l))
    
    

