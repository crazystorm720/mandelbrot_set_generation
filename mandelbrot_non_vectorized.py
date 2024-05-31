import numpy as np
import matplotlib.pyplot as plt
import time

# Function to generate the Mandelbrot set (non-vectorized)
def mandelbrot_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations):
    image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            c_real = Re_min + x * (Re_max - Re_min) / width
            c_imag = Im_min + y * (Im_max - Im_min) / height
            z_real = 0
            z_imag = 0
            n = 0
            while n < max_iterations and z_real * z_real + z_imag * z_imag < 4:
                z_real_temp = z_real * z_real - z_imag * z_imag + c_real
                z_imag = 2 * z_real * z_imag + c_imag
                z_real = z_real_temp
                n += 1
            image[y, x] = n
    return image

def run_and_save_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations):
    start_time = time.time()
    image = mandelbrot_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations)
    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    plt.imshow(image, extent=(Re_min, Re_max, Im_min, Im_max), cmap='hot')
    plt.colorbar()
    plt.savefig('results/mandelbrot_non_vectorized.png')
    return execution_time