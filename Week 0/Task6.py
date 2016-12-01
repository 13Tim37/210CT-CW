nList = input("Enter a list of integers seperated by spaces: ").split()

mn = nList[0]
mx = nList[0]
for i in nList:
    if i < mn:
        mn = i
    if i > mx:
        mx = i

print(("Min is {} at position {}.").format(mn, nList.index(mn)+1))
print(("Max is {} at position {}.").format(mx, nList.index(mx)+1))
