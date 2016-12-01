labyrinth = [
    0[0,0,0,0,0,0],
    1[0,1,1,1,0,0],
    2[0,1,0,1,0,0],
    3[0,1,1,1,1,0],
    4[0,0,1,0,1,0],
    5[0,0,0,0,1,0]
]

i = 1
j = 1

exitx = 5
exity = 4

px = i
py = j

top = labyrinth[py-1[px]]
right = labyrinth[py[px+1]]
bottom = labyrinth[py+1[px]]
left = labyringth[py[px-1]]


