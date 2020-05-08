
height = 20#must be divisihble by 2
max_iteration = 99

def scale(val, src, dst):#tuple lowest possible - highest possible,,,,,tuple new lowest - new highest
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

screen2 = []

for row in range(height):
    screen2.append([])

for col in range(height):
    for x in range(int(height/2)):
        screen2[col].append([])

print(screen2[0])#columns, height SHOULD BE HALF OF THE HEIGHT
print(len(screen2))#rows heigh

#     r2 c3
#screen2[1][2]=2

for row in range(height):
    for col in range(int(height/2)):
        x0 = scale(row, (0,height), (-2.5,1))###--If it dosent work try edit these lines
        y0 = scale(col, (0,int(height/2)), (-1,1))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
        x = 0
        y = 0
        iteration = 0
        while x*x + y*y <= 2*2 and iteration < max_iteration:
            xtemp = x*x -y*y + x0
            y = 2*x*y + y0
            x = xtemp
            iteration += 1

        screen2[row][col] = iteration

for x in screen2:
    print(x)
