import pygame
import pygame.gfxdraw


width = 300
height = 300#must be divisihble by 2
zoom_window = 50
max_iteration = 255

# y01 = -0.19919
# y02 = -0.199155
#
# x01 = -0.6795495
# x02 = -0.6795145

#normal
y01 = -2.25#u,1
y02 = 1#d,2

x01 = -1.5#l,3
x02 = 1.5#r,4

colors = []

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


# r = 0
# g = 0
# b = 0
# for x in range(254):
#     colors.append((r,g,b))
#     r += 5
#     g += 5
#     b += 5
#     if r > 255 or g > 255 or b > 255:
#         r = 0
#         g = 0
#         b = 0
# colors.append((0,0,0))



def scale(val, src, dst):#tuple lowest possible - highest possible,,,,,tuple new lowest - new highest
    return float(((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0])#maybe remove float?






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


#get font
font = pygame.font.SysFont(None, 14)
# +--- Calculate screen grid numbers ---+
def generate_grid():
    for row in range(height):
        for col in range(width):
            x0 = scale(row, (0,height), (y01,y02))###--If it dosent work try edit these lines
            y0 = scale(col, (0,width), (x01,x02))#####  +--col,row,order of scaling(arrangement(a,b)(b,a)), min and max values---+  all these can fail
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

generate_grid()
# +--draw pixels --+
# +-- NOTE IF YOU WANT ZOOM PUT IN LOOP --+
def draw_image():
    for row in range(height):
        for column in range(width):
            color1 = colors[int(scale(screen2[row][column], (0,max_iteration),(0,len(colors)-1)))]
            pygame.gfxdraw.pixel(screen, column, row, color1)

draw_image()
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

            #ERROR CAUSES IMAGES TO APPEAR ON LEFT OF INTENDED AREA
            #need to know where those pixels lie on the complex plane
            top = scale(pos[1]+zoom_window, (0,height), (y01,y02))
            bottom = scale(pos[1]-zoom_window, (0,height), (y01,y02))

            left = scale(pos[0]-zoom_window, (0,width), (x01,x02))
            right = scale(pos[0]+zoom_window, (0,width), (x01,x02))

            print(y01,y02,x01,x02)

            y01 = bottom
            y02 = top
            x01 = right
            x02 = left





            print("t+b")
            print(top,bottom)
            print("l+r")
            print(left, right)

            generate_grid()



            draw_image()


            print("done")

    draw_image()

    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0,255,0), (pos[0]-zoom_window,pos[1]-zoom_window,100,100), 1)

    top = scale(pos[1]+zoom_window, (0,height), (y01,y02))
    bottom = scale(pos[1]-zoom_window, (0,height), (y01,y02))
    left = scale(pos[0]-zoom_window, (0,width), (x01,x02))
    right = scale(pos[0]+zoom_window, (0,width), (x01,x02))

    img = font.render(f'x1:{x01} x2:{x02} y1:{y01} y2:{y02}', True, (255,255,255))
    img2 = font.render(f'x1:{top} x2:{bottom} y1:{left} y2:{right}', True, (255,255,255))
    screen.blit(img, (0, 0))
    screen.blit(img2, (0, 20))
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
