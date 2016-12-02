from random import randint

def shuffle_list(int_list):
    # Using fisher-yates shuffle algorithm.
    shuffled = []                                                            #1

    def random_arrange(int_list):
        # Choose a random index between 0 and the last item in the list.
        x = randint(0, len(int_list)-1)                                      #n
        # Append this item to the shuffled list.
        shuffled.append(int_list[x])                                         #n
        # Remove item and swap last number.
        int_list[x] = int_list[len(int_list)-1]                              #n
        del int_list[-1]                                                     #n

        if len(int_list) > 0:                                                #n
            return(random_arrange(int_list))                                 #n
        else:                                                                #1
            return shuffled                                                  #1
        
    return(random_arrange(int_list))                                         #1

def init():
    # If value error occurs user has entered non-integers into the input.
    # We let them know and retry the input.
    try:
        int_list = list(map(int, input("Enter a list of integers seperated by ',' >> ").split(',')))
    except ValueError or SyntaxError:
        print('Only enter a list of integers!')
        int_list = init()
    return int_list

int_list = init()

print('The original list is: ' + str(int_list))                              
print('The shuffled list is: ' + str(shuffle_list(int_list)))                

# Total = 6n + 4
# Big O = O(n)
