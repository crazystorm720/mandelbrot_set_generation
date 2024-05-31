import os
import platform
from datetime import datetime
from mandelbrot_non_vectorized import run_and_save_non_vectorized
from mandelbrot_vectorized import run_and_save_vectorized

# Get system name and current date
system_name = platform.node()
current_date = datetime.now().strftime('%Y%m%d')
results_dir = f'results/{system_name}_{current_date}'

# Create results directory if it doesn't exist
os.makedirs(results_dir, exist_ok=True)

# Parameters
width, height = 1000, 1000
Re_min, Re_max = -2.0, 1.0
Im_min, Im_max = -1.5, 1.5
max_iterations = 1000

# Run non-vectorized method and capture execution time
non_vectorized_time = run_and_save_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir)

# Run vectorized method and capture execution time
vectorized_time = run_and_save_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir)

# Generate analysis report
with open(os.path.join(results_dir, 'analysis.md'), 'w') as f:
    f.write("# Mandelbrot Set Generation Results\n\n")
    
    f.write("## Non-Vectorized Method\n")
    f.write(f"![Non-Vectorized Mandelbrot]({results_dir}/mandelbrot_non_vectorized.png)\n")
    f.write(f"Execution time: {non_vectorized_time:.2f} ms\n")
    f.write("The non-vectorized method iterates over each pixel individually, which can be slow for large images.\n\n")
    
    f.write("## Vectorized Method\n")
    f.write(f"![Vectorized Mandelbrot]({results_dir}/mandelbrot_vectorized.png)\n")
    f.write(f"Execution time: {vectorized_time:.2f} ms\n")
    f.write("The vectorized method leverages numpy's array operations to perform computations on entire arrays at once, significantly speeding up the process.\n")

