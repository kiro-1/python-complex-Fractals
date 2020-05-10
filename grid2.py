import pygame
import colorsys
import pygame.gfxdraw
import time
height = 600#must be divisihble by 2
max_iteration = 99
aspect = 2

x01 = -0.20
x02 = -0.19

y01 = -0.68
y02 = -0.67

def scale(val, src, dst):#tuple lowest possible - highest possible,,,,,tuple new lowest - new highest
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]



screen2 = []

for row in range(height):
    screen2.append([])

for col in range(height):
    for x in range(int(height/2)):
        screen2[col].append([])


# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [int(height/aspect), height]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Fractal")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# +--- Calculate screen grid numbers ---+
for row in range(height):
    for col in range(int(height/aspect)):
        x0 = scale(row, (0,height), (x01,x02))###--If it dosent work try edit these lines
        y0 = scale(col, (0,int(height/aspect)), (y01,y02))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
        x = 0
        y = 0
        iteration = 0
        while x*x + y*y <= 2*2 and iteration < max_iteration:
            xtemp = x*x -y*y + x0
            y = 2*x*y + y0
            x = xtemp
            iteration += 1

        screen2[row][col] = iteration
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop




        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # User clicks the mouse. Get the position
        #     pos = pygame.mouse.get_pos()
        #     # Change the x/y screen coordinates to grid coordinates
        #     column = pos[0] // (WIDTH)
        #     row = pos[1] // (HEIGHT)
        #     # Set that location to one
        #     grid[row][column] = 1
        #     print("Click ", pos, "Grid coordinates: ", row, column)



    # Set the screen background

    #screen.fill(BLACK)



    # Draw the grid
    # for row in range(height):
    #     for column in range(int(height/aspect)):
    #         color = (scale(screen2[row][column], (0,max_iteration), (80,1)), 0, 100)
    #         pygame.draw.rect(screen,
    #                         color,
    #                          [( WIDTH) * column,
    #                           (HEIGHT) * row,
    #                           WIDTH,
    #                           HEIGHT])
    for row in range(height):
        for column in range(int(height/aspect)):
            color = (scale(screen2[row][column], (0,max_iteration), (80,1)), 0, 100)
            pygame.gfxdraw.pixel(screen, column, row, color)



    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    time.sleep(60)
    done = True

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
