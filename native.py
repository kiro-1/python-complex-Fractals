
size = 30
max_iteration = 99

def scale(val, src, dst):#tuple lowest possible - highest possible,,,,,tuple new lowest - new highest
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

screen = []

for row in range(size):
    screen.append([])
for x in range(size):
    for i in range(size):
        screen[i].append([])

#     r2 c3
#screen[1][2]=2

for row in range(size):
    for col in range(size):
        x0 = scale(row, (0,size), (-2.5,1))###--If it dosent work try edit these lines
        y0 = scale(col, (0,size), (-1,1))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
        x = 0
        y = 0
        iteration = 0
        while x*x + y*y <= 2*2 and iteration < max_iteration:
            xtemp = x*x -y*y + x0
            y = 2*x*y + y0
            x = xtemp
            iteration += 1

        screen[row][col] = iteration

for x in screen:
    print(x)
