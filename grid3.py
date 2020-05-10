import pygame

import pygame.gfxdraw
import random
width = 200
height = 200#must be divisihble by 2
max_iteration = 255

# x01 = -0.19919
# x02 = -0.199155
#
# y01 = -0.6795495
# y02 = -0.6795145

# x01 = -0.20
# x02 = -0.19
#
# y01 = -0.68
# y02 = -0.67

#normal
x01 = -2.25
x02 = 0.75

y01 = -1.5
y02 = 1.5

colors = []

colors.append((0,0,0))
colors.append((12, 3, 13))
colors.append((25, 7, 26))
colors.append((15, 3, 33))
colors.append((9, 1, 47))
colors.append((7, 2, 59))
colors.append((4, 4, 73))
colors.append((2, 5, 88))
colors.append((0, 7, 100))
colors.append((6, 26, 116))
colors.append((12, 44, 138))
colors.append((19, 62, 150))
colors.append((24, 82, 177))
colors.append((42, 92, 189))
colors.append((57, 125, 209))
colors.append((85, 140, 215))
colors.append((134, 181, 229))
colors.append((167, 200, 235))
colors.append((211, 236, 248))
colors.append((228, 234, 215))
colors.append((241, 233, 191))
colors.append((245, 215, 100))
colors.append((248, 201, 95))
colors.append((252, 185, 42))
colors.append((255, 170, 0))
colors.append((232, 137, 0))
colors.append((204, 128, 0))
colors.append((175, 109, 0))
colors.append((153, 87, 0))
colors.append((125, 65, 0))
colors.append((106, 52, 3))
colors.append((50, 25, 3))

colors.append((106, 52, 3))
colors.append((12, 3, 13))
colors.append((25, 7, 26))
colors.append((15, 3, 33))
colors.append((9, 1, 47))
colors.append((7, 2, 59))
colors.append((4, 4, 73))
colors.append((2, 5, 88))
colors.append((0, 7, 100))
colors.append((6, 26, 116))
colors.append((12, 44, 138))
colors.append((19, 62, 150))
colors.append((24, 82, 177))
colors.append((42, 92, 189))
colors.append((57, 125, 209))
colors.append((85, 140, 215))
colors.append((134, 181, 229))
colors.append((167, 200, 235))
colors.append((211, 236, 248))
colors.append((228, 234, 215))
colors.append((241, 233, 191))
colors.append((245, 215, 100))
colors.append((248, 201, 95))
colors.append((252, 185, 42))
colors.append((255, 170, 0))
colors.append((232, 137, 0))
colors.append((204, 128, 0))
colors.append((175, 109, 0))
colors.append((153, 87, 0))
colors.append((125, 65, 0))

colors.append((0,0,0))

def scale(val, src, dst):#tuple lowest possible - highest possible,,,,,tuple new lowest - new highest
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]



def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))



screen2 = []

for row in range(height):
    screen2.append([])

for col in range(height):
    for x in range(width):
        screen2[col].append([])


# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [width, height]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Fractal")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# +--- Calculate screen grid numbers ---+
for row in range(height):
    for col in range(width):
        x0 = scale(row, (0,height), (x01,x02))###--If it dosent work try edit these lines
        y0 = scale(col, (0,width), (y01,y02))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
        x = 0
        y = 0
        iteration = 0
        while x*x + y*y <= 2*2 and iteration < max_iteration:
            xtemp = x*x -y*y + x0
            y = 2*x*y + y0
            x = xtemp
            iteration += 1

        screen2[row][col] = iteration
        print(str(int(scale(row, (0, width), (0,100))))+"."+str(int(scale(col, (0, height), (0,100))))+"%")
# +--draw pixels --+
# +-- NOTE IF YOU WANT ZOOM PUT IN LOOP --+
for row in range(height):
    for column in range(width):
        color = colors[int(scale(screen2[row][column], (0,max_iteration),(0,32)))]
        pygame.gfxdraw.pixel(screen, column, row, color)
# -------- Main Program Loop -----------


def gridcoord_to_complexcoord(x,y):
    new_x = scale(x, (0,height), (x01,x02))
    new_y = scale(y, (0,height), (y01,y02))
    h = (new_x,new_y)
    return h
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop




        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column1 = pos[0] // (width)
            row1 = pos[1] // (height)

            print("Click ", pos, )


            lt = (pos[0] - 10, pos[1] + 10)
            # rt = (pos[0] + 10, pos[1] + 10)
            # lb = (pos[0] - 10, pos[1] - 10)
            rb = (pos[0] + 10, pos[1] - 10)

            #print(str(lt)+"         "+str(rt)+"\n\n\n"+str(lb)+"        "+str(rb))
            print()
            print(gridcoord_to_complexcoord(lt[0], lt[1]), gridcoord_to_complexcoord(rb[0], rb[1]))

            new_lt = gridcoord_to_complexcoord(lt[0], lt[1])
            new_rb = gridcoord_to_complexcoord(rb[0], rb[1])


            for row in range(height):
                for col in range(width):
                    x0 = scale(row, (0,height), (new_lt[0],new_lt[1]))###--If it dosent work try edit these lines
                    y0 = scale(col, (0,width), (new_rb[0],new_rb[1]))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
                    x = 0
                    y = 0
                    iteration = 0
                    while x*x + y*y <= 2*2 and iteration < max_iteration:
                        xtemp = x*x -y*y + x0
                        y = 2*x*y + y0
                        x = xtemp
                        iteration += 1

                    screen2[row][col] = iteration
                    print(str(int(scale(row, (0, width), (0,100))))+"."+str(int(scale(col, (0, height), (0,100))))+"%")



            for row in range(height):
                for column in range(width):
                    color = colors[int(scale(screen2[row][column], (0,max_iteration),(0,32)))]
                    pygame.gfxdraw.pixel(screen, column, row, color)


    # Set the screen background

    #screen.fill(BLACK)



    # Draw the grid
    # for row in range(height):
    #     for column in range(height):
    #         color = (scale(screen2[row][column], (0,max_iteration), (80,1)), 0, 100)
    #         pygame.draw.rect(screen,
    #                         color,
    #                          [( WIDTH) * column,
    #                           (HEIGHT) * row,
    #                           WIDTH,
    #                           HEIGHT])




    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
