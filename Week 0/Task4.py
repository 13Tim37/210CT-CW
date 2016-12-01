s = str(input("Enter string to process: "))
b = int(input("Enter beginning position: "))
l = int(input("Enter length to delete: "))

def delSubstring(s,b,l):
    print("Original string: {}".format(s))
    s[b:(b+l)]
    s = s[0:b] + s[(b+l):-1] + s[-1]
    return s

e = delSubstring(s,b,l)
print("Edited string: {}".format(e))
