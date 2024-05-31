import numpy as np
import matplotlib.pyplot as plt
import time
import os
import tracemalloc
import psutil

# Function to generate the Mandelbrot set (vectorized)
def mandelbrot_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations):
    Re = np.linspace(Re_min, Re_max, width)
    Im = np.linspace(Im_min, Im_max, height)
    C_real, C_imag = np.meshgrid(Re, Im)
    Z_real = np.zeros_like(C_real)
    Z_imag = np.zeros_like(C_imag)
    iterations = np.zeros_like(C_real, dtype=int)
    iteration_counts = np.zeros_like(C_real)

    for i in range(max_iterations):
        mask = Z_real * Z_real + Z_imag * Z_imag < 4.0
        Z_real_temp = np.where(mask, Z_real * Z_real - Z_imag * Z_imag + C_real, Z_real)
        Z_imag = np.where(mask, 2 * Z_real * Z_imag + C_imag, Z_imag)
        Z_real = Z_real_temp
        iterations[mask] = i
        iteration_counts[mask] = i
    
    return iterations, iteration_counts

def run_and_save_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir):
    tracemalloc.start()
    start_time = time.time()
    process = psutil.Process(os.getpid())

    image, iteration_counts = mandelbrot_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations)

    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    memory_usage = tracemalloc.get_traced_memory()[1] / (1024 ** 2)  # in MB
    cpu_usage = process.cpu_percent()

    tracemalloc.stop()

    # Plot and save the Mandelbrot set
    plt.figure(figsize=(10, 10), dpi=300)
    plt.imshow(image, extent=(Re_min, Re_max, Im_min, Im_max), cmap='inferno', interpolation='bilinear')
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Set (Vectorized)')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.savefig(os.path.join(results_dir, 'mandelbrot_vectorized.png'))
    plt.close()

    return execution_time, memory_usage, cpu_usage, iteration_counts
