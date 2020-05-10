import time
size = 100
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


x01 = -0.20
x02 = -0.19

y01 = -0.68
y02 = -0.67

# x01 = -2.5
# x02 = 1
#
# y01 = -1
# y02 = 1

loop = 0
while True:

    for row in range(size):
        for col in range(size):
            x0 = scale(row, (0,size), (x01,x02))###--If it dosent work try edit these lines
            y0 = scale(col, (0,size), (y01,y02))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
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


    print("\n\n\n")

    # x01 -= 0.1
    # x02 -= 0.1
    # y01 -= 0.1
    # y02 -= 0.1


    loop +=1

    if loop == 1:
        break
