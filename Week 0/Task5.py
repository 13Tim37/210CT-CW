y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day of month: "))

months = [31,28,31,30,31,30,31,31,30,31,30,31]

ly = False
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
    ly = True
    months[1] = 29

x = 0
while x < m-1:
    d = d + months[x]
    x = x + 1

if ly == True:
    r = 366 - (d - 1)
else:
    r = 365 - (d - 1)

print(("{} days in, with {} days left.").format(d-1, r))
