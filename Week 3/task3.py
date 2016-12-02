s = str(input('Enter a string: '))

def removeVowels(s, i=0):
    s = list(s)
    vowels = ['a','e','i','o','u']
    if s[i] in vowels:
        s[i] = ''
    if i == len(s)-1:
        return s
    else:
        return ''.join(removeVowels(s,i+1))

print(removeVowels(s))
