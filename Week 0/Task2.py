ax = int(input("Enter x co-ord for point a: "))
ay = int(input("Enter y co-ord for point a: "))
bx = int(input("Enter x co-ord for point b: "))
by = int(input("Enter y co-ord for point b: "))
cx = int(input("Enter x co-ord for point c: "))
cy = int(input("Enter y co-ord for point c: "))

px = int(input("Enter x co-ord for point p: "))
py = int(input("Enter y co-ord for point p: "))

right = max(ax,bx,cx)
left = min(ax,bx,cx)

top = max(ay,by,cy)
bottom = min(ay,by,cy)

if px > right:
    h = "right"
elif px < left:
    h = "left"
elif px <= right and px >= left:
    h = ""
else:
    h = ""

if py > top:
    v = "top"
elif py < bottom:
    v = "bottom"
elif py <= top and py >= bottom:
    v = ""
else:
    v = ""

print("The point is {} {} of the triangle.".format(v, h))






