import os
import platform
from datetime import datetime
from mandelbrot_non_vectorized import run_and_save_non_vectorized
from mandelbrot_vectorized import run_and_save_vectorized
import subprocess

# Get system name and current date with minutes
system_name = platform.node()
current_date = datetime.now().strftime('%Y%m%d_%H%M')
results_dir = f'results/{system_name}_{current_date}'

# Create results directory if it doesn't exist
os.makedirs(results_dir, exist_ok=True)

# Parameters
width, height = 1000, 1000
Re_min, Re_max = -2.0, 1.0
Im_min, Im_max = -1.5, 1.5
max_iterations = 1000

# Run non-vectorized method and capture metrics
non_vectorized_time, non_vectorized_memory, non_vectorized_cpu, non_vectorized_iterations = run_and_save_non_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir)

# Run vectorized method and capture metrics
vectorized_time, vectorized_memory, vectorized_cpu, vectorized_iterations = run_and_save_vectorized(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir)

# Generate analysis report
subprocess.run(['python', 'src/generate_analysis.py', str(non_vectorized_time), str(vectorized_time), str(non_vectorized_memory), str(vectorized_memory), str(non_vectorized_cpu), str(vectorized_cpu), results_dir])
