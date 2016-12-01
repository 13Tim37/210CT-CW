s = str(input('Please enter a sentence: ')) + ' ' #1

def reverseSentence(s):                           
    s_list = []                                   #1
    i, x = 0, 0                                   #1
    for letter in s:                              #n
        x = x + 1                                 #n
        if letter == ' ' or x == len(s):          #n
            s_list.insert(0, s[i:x])              #n
            i = x                                 #n
        else:                                     #n
            continue                              #n
        
    return ('').join(s_list)                    

print(reverseSentence(s))

#Function has a big O notation of O(n)

