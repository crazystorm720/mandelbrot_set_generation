import numpy as np
import matplotlib.pyplot as plt
import time
import os

# Function to generate the Mandelbrot set (vectorized)
def mandelbrot_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations):
    Re = np.linspace(Re_min, Re_max, width)
    Im = np.linspace(Im_min, Im_max, height)
    C_real, C_imag = np.meshgrid(Re, Im)
    Z_real = np.zeros_like(C_real)
    Z_imag = np.zeros_like(C_imag)
    iterations = np.zeros_like(C_real, dtype=int)

    for i in range(max_iterations):
        mask = Z_real * Z_real + Z_imag * Z_imag < 4.0
        Z_real_temp = np.where(mask, Z_real * Z_real - Z_imag * Z_imag + C_real, Z_real)
        Z_imag = np.where(mask, 2 * Z_real * Z_imag + C_imag, Z_imag)
        Z_real = Z_real_temp
        iterations[mask] = i
    
    return iterations

def run_and_save_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir):
    start_time = time.time()
    image = mandelbrot_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations)
    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    plt.imshow(image, extent=(Re_min, Re_max, Im_min, Im_max), cmap='hot')
    plt.colorbar()
    plt.savefig(os.path.join(results_dir, 'mandelbrot_vectorized.png'))
    return execution_time

