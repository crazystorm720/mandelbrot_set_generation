import numpy as np
import matplotlib.pyplot as plt
import time
import os
import tracemalloc
import psutil

# Function to generate the Mandelbrot set (non-vectorized)
def mandelbrot_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations):
    image = np.zeros((height, width))
    iteration_counts = np.zeros((height, width))
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
            iteration_counts[y, x] = n
    return image, iteration_counts

def run_and_save_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir):
    tracemalloc.start()
    start_time = time.time()
    process = psutil.Process(os.getpid())

    image, iteration_counts = mandelbrot_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations)

    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    memory_usage = tracemalloc.get_traced_memory()[1] / (1024 ** 2)  # in MB
    cpu_usage = process.cpu_percent()

    tracemalloc.stop()

    # Plot and save the Mandelbrot set
    plt.figure(figsize=(10, 10), dpi=300)
    plt.imshow(image, extent=(Re_min, Re_max, Im_min, Im_max), cmap='inferno', interpolation='bilinear')
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Set (Non-Vectorized)')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.savefig(os.path.join(results_dir, 'mandelbrot_non_vectorized.png'))
    plt.close()

    return execution_time, memory_usage, cpu_usage, iteration_counts
