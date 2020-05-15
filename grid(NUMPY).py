import pygame
import pygame.gfxdraw

import numpy as np


zoom_window = 100

size = 1000
n = 1000#number of iterations
r = 2 # escape radius (must be greater than 2)

x1 = -2
x2 = 1
y1 = -1.5
y2 = 1.5

previous = [[-2,1,-1.5,1.5]]

colors = []

#REMOVE FOR LOOP FOR REALISTIC COLOURING
num_of_colours = 30
for x in range(int(n/(num_of_colours-1))):
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

pygame.init()
# +-- Create An Empty Global Variable --+
T = np.empty([size,size])

backup = pygame.Surface((size,size))
# +-- REMOVE --+ #

#replace with more efficient solution
def scale(val, src, dst):
    return float(((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0])


screen = pygame.display.set_mode([size,size])

# Set title of screen
pygame.display.set_caption("Fractal")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#get font
font = pygame.font.SysFont(None, 14)
# +--- Calculate screen grid numbers ---+
def Generate_grid():
    global T
    x = np.linspace(x1, x2,size)
    y = np.linspace(y1, y2,size)

    A, B = np.meshgrid(x, y)

    C = A + B * 1j

    Z = np.zeros_like(C)
    T = np.zeros(C.shape)

    for k in range(n):
        M = abs(Z) < r
        Z[M] = Z[M] ** 2 + C[M]
        T[M] = k + 1

Generate_grid()
# +--draw pixels --+
# +-- NOTE IF YOU WANT ZOOM PUT IN LOOP --

def draw_image():

    for row in range(size):

        for column in range(size):

            color1 = colors[int(scale(T[row][column], (0,n),(0,len(colors)-1)))]
            pygame.gfxdraw.pixel(backup, column, row, color1)

    img = font.render(f'x1:{x1} x2:{x2} y1:{y1} y2:{y2}', True, (255,255,255))
    backup.blit(img, (0, 0))

draw_image()

print("- b go back one zoom generation\n- r reset the zoom")
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates

            print("Click ", pos, )

            top = scale(pos[1]+zoom_window/2, (0,size), (y1,y2))
            bottom = scale(pos[1]-zoom_window/2, (0,size), (y1,y2))

            left = scale(pos[0]-zoom_window/2, (0,size), (x1,x2))
            right = scale(pos[0]+zoom_window/2, (0,size), (x1,x2))


            y1 = bottom
            y2 = top
            x1 = left
            x2 = right

            previous.append([y1,y2,x1,x2])

            Generate_grid()
            draw_image()

            print("done")


        elif event.type == pygame.KEYDOWN:#if a keystroke has been detected

            if event.key == pygame.K_b:
                try:
                    previous.pop()
                    num = len(previous)-1
                    y1 = previous[num][0]
                    y2 = previous[num][1]
                    x1 = previous[num][2]
                    x2 = previous[num][3]
                    Generate_grid()
                    draw_image()
                    print("done")
                except:
                    previous.append([-2,1,-1.5,1.5])

            if event.key == pygame.K_r:
                x1,x2,y1,y2 = -2,1,-1.5,1.5
                Generate_grid()
                draw_image()
                print("done")


    screen.blit(backup, (0,0))

    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0,255,0), (int(pos[0]-zoom_window/2),int(pos[1]-zoom_window/2),zoom_window,zoom_window), 1)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
