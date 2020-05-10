# THIS CODE IS PROVIDED "AS IS". IN NO EVENT SHALL I, BIG.B.RADICAL, BE
# LIABLE FOR ANY KIND OF LOSS OR DAMAGE ARISING OUT OF THE USE, ABUSE OR THE
# INABILITY TO USE THIS CODE. USE IT AT YOUR OWN RISK!

# Version 1.0

import os, pygame, math, cProfile
from pygame.locals import *
from numba import jit
import numpy as np

class Mandelbrot:

    def _calculate_min_max(s):
        s.x_min, s.x_max = s.center[0] - s.x_range / 2, s.center[0] + s.x_range / 2
        s.y_min, s.y_max = s.center[1] - s.y_range / 2, s.center[1] + s.y_range / 2

    def _calculate_y_range(s):
        s.y_range = s.win_height * s.x_range / s.win_width

    def __init__(s, win_dims, max_iter, threshold, center, x_range, color_algorithm, color_multiplier, palettes, current_palette):
        s.win_width, s.win_height = win_dims
        s.max_iter = max_iter
        s.threshold = threshold
        s.center = center
        s.x_range = x_range
        s._calculate_y_range()
        s.scroll_rate = 1
        s.zoom_factor = 1
        s._calculate_min_max()
        s.current_palette = current_palette
        s.color_algorithm = color_algorithm
        s.color_multiplier = color_multiplier
        s.palettes = palettes

    @staticmethod
    def _get_color(palette_colors, palette_indices, index):
        index = index % 1
        for i in range(len(palette_indices)):
            if (index >= palette_indices[i] and index <= palette_indices[i+1]):
                index_start = palette_indices[i]
                index_end = palette_indices[i+1]
                new_index = (index - index_start) / (index_end - index_start)
                color_start = palette_colors[i]
                color_end = palette_colors[i+1]
                break

        return Color(round(new_index * (color_end[0] - color_start[0]) + color_start[0]),
                     round(new_index * (color_end[1] - color_start[1]) + color_start[1]),
                     round(new_index * (color_end[2] - color_start[2]) + color_start[2]), 255)

    def cycle_current_palette(s):
        s.current_palette = (s.current_palette + 1) % len(s.palettes)
        print('Cycling to palette:', s.current_palette)


    @staticmethod
    @jit
    def _inner_calculation(x, y, max_iter, threshold_sqr):
        C = complex(x,y)
        z = 0+0j
        iter_count = 0                    # Reset iteration count for each pixel
        for _ in range(0, max_iter):
            z = z*z + C                  # f(z) = z^2 + C
            iter_count += 1
            z_mag_sqr = z.real*z.real + z.imag*z.imag
            if z_mag_sqr > threshold_sqr:
                break
        return z, iter_count

    def _get_color_index(s, abs_val, iter_count):
        temp_index = abs(iter_count - math.log(math.log(abs_val), 2))  # Smoothing
        if (s.color_algorithm == 0): return 1 / temp_index * s.color_multiplier  # Alg 0
        else: return temp_index * s.color_multiplier / 500  # Alg 1

    def draw(s, surface):
        print('Redrawing image...')
        pixel_array = pygame.PixelArray(surface)
        threshold_sqr = s.threshold * s.threshold
        x_coords = np.linspace(s.x_min, s.x_max, s.win_width)
        y_coords = np.linspace(s.y_max, s.y_min, s.win_height)
        mand = (s._inner_calculation(x, y, s.max_iter, threshold_sqr) for y in y_coords for x in x_coords)
        count = 0
        for z,iter_count in mand:
            abs_val = abs(z)
            if abs_val <= 2:
                pix_color = Color(0,0,0,255)  # These are in the set
            else:
                color_index = s._get_color_index(abs_val, iter_count)
                pix_color = s._get_color(s.palettes[s.current_palette][0], s.palettes[s.current_palette][1], color_index)
            pixel_array[count % s.win_width, count // s.win_width] = pix_color
            count += 1
        del pixel_array
        print('Image redrawn')

    def _move_center(s, x_pixels, y_pixels):
        s.center[0] += x_pixels * (s.x_range / s.win_width)
        s.center[1] += y_pixels * (s.y_range / s.win_height)
        s._calculate_min_max()

    def scroll(s, x_scroll, y_scroll, surface):
        x_pixels = x_scroll * s.scroll_rate
        y_pixels = y_scroll * s.scroll_rate
        surface.scroll(x_pixels, y_pixels)
        s._move_center(-x_pixels, y_pixels)

    def increase_scroll_rate(s):
        s.scroll_rate *= 2
        print('Scroll Rate:', s.scroll_rate)

    def decrease_scroll_rate(s):
        if s.scroll_rate > 1:
            s.scroll_rate //= 2
        print('Scroll Rate:', s.scroll_rate)

    def zoom(s, surface):
        s.x_range /= s.zoom_factor
        s._calculate_y_range()
        s._calculate_min_max()
        s.draw(surface)

    def increase_zoom_factor(s):
        s.zoom_factor *= 1.1
        print('Zoom Factor:', s.zoom_factor)

    def decrease_zoom_factor(s):
        s.zoom_factor /= 1.1
        print('Zoom Factor:', s.zoom_factor)

    def print_info(s):
        print('Mandelbrot Position:')
        print('Center:', s.center)
        print('X-Min-Max:', s.x_min, s.x_max)
        print('Y-Min-Max:', s.y_min, s.y_max)
        print('Mandelbrot Variables:')
        print('Max Iterations:', s.max_iter)
        print('Threshold:', s.threshold)

    def increase_color_multiplier(s):
        s.color_multiplier *= 1.1
        print('Color Multiplier:', s.color_multiplier)

    def increase_max_iter(s):
        s.max_iter *= 2
        print('Max Iterations:', s.max_iter)

    def increase_threshold(s):
        s.threshold *= 1.1
        print('Threshold:', s.threshold)

    def decrease_color_multiplier(s):
        s.color_multiplier /= 1.1
        print('Color Multiplier:', s.color_multiplier)

    def decrease_max_iter(s):
        s.max_iter /= 2
        print('Max Iterations:', s.max_iter)

    def decrease_threshold(s):
        s.threshold /= 1.1
        print('Threshold:', s.threshold)

    def cycle_color_algorithm(s):
        s.color_algorithm = (s.color_algorithm + 1) % 2
        print('Cycling to color_algorithm:', s.color_algorithm)


#------------------------------------------------------------------------------------------
def get_int_from_user(prompt):
    print(prompt)
    return int(input())

def keyboard_input(key, mandelbrot, surface):
    if key == pygame.K_LEFT:
        mandelbrot.scroll(1, 0, surface)
    elif key == pygame.K_RIGHT:
        mandelbrot.scroll(-1, 0, surface)
    elif key == pygame.K_UP:
        mandelbrot.scroll(0, 1, surface)
    elif key == pygame.K_DOWN:
        mandelbrot.scroll(0, -1, surface)
    elif key == pygame.K_d:
        #cProfile.runctx('mandelbrot.draw(surface)', None, locals())
        mandelbrot.draw(surface)
    elif key == pygame.K_1:
        mandelbrot.decrease_scroll_rate()
    elif key == pygame.K_2:
        mandelbrot.increase_scroll_rate()
    elif key == pygame.K_3:
        mandelbrot.decrease_color_multiplier()
    elif key == pygame.K_4:
        mandelbrot.increase_color_multiplier()
    elif key == pygame.K_5:
        mandelbrot.decrease_max_iter()
    elif key == pygame.K_6:
        mandelbrot.increase_max_iter()
    elif key == pygame.K_7:
        mandelbrot.decrease_threshold()
    elif key == pygame.K_8:
        mandelbrot.increase_threshold()
    elif key == pygame.K_9:
        mandelbrot.decrease_zoom_factor()
    elif key == pygame.K_0:
        mandelbrot.increase_zoom_factor()
    elif key == pygame.K_z:
        mandelbrot.zoom(surface)
    elif key == pygame.K_s:
        pygame.image.save(surface, 'image.png')
    elif key == pygame.K_p:
        mandelbrot.print_info()
    elif key == pygame.K_c:
        mandelbrot.cycle_current_palette()
    elif key == pygame.K_a:
        mandelbrot.cycle_color_algorithm()


def main():
    palettes = (
                  ( ((255,0,0),(0,255,0),(0,0,255),(255,0,0)),            # RGB
                    (0,0.33,0.66,1) ),
                  ( ((255,255,0),(0,255,255),(255,0,255), (255,255,0)),       # Cotton Candy
                    (0,0.33,0.66,1) ),
                  ( ((255,0,0),(255,128,0),(255,255,0), (0,255,0), (0,255,255), (0,68,255), (255,0,255), (255,0,0)), # Rainbow-ish
                    (0, 0.14, 0.29, 0.44, 0.59, 0.74, 0.89, 1) ),
                  ( ((255,255,255), (0, 0, 0), (32, 32, 32), (0, 0, 255), (255,0,0), (255,255,0), (255,255,255)), # Fire
                    (0, 0.16, 0.33, 0.50, 0.67, 0.84, 1) )
                )
    win_dims = 100, 100  # width, height
    pygame.init()
    surface = pygame.display.set_mode(win_dims)
    pygame.display.set_caption('Mandelbrot')
    mandelbrot = Mandelbrot(win_dims, 32, 100, [0, 0], 4, 0, 5, palettes, 2)
    mandelbrot.draw(surface)

    going = True
    while going:    # Main game loops

        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == pygame.KEYDOWN:
                keyboard_input(event.key, mandelbrot, surface)

        pygame.display.update() # Would be better if only on scroll, zoom, draw, or color change

    pygame.quit()


main()

# Properties of logarithms:
# log_a(x) = log_b(x) / log_b(a)
# log_a(xy) = log_a(x) + log_a(y)
# log_a(x/y) = log_a(x) - log_a(y)
# log_a(xr) = r * log_a(x)
