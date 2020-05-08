import numpy as np
#import matplotlib.pyplot as plt



def mandelbrot( h,w, maxit=100 ):
    y,x = np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j]
    #print(y,x)
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime




h = input("please enter the height in units of your mandelbrot set: ")
w = input("please enter the width in units of your mandelbrot set: ")
m = mandelbrot(int(h),int(w))
with open("thebrot.txt", 'w') as f:
    for x in m:

        f.write(str(x))

# plt.imshow(mandelbrot(800,800))
# plt.show()
