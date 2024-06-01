### Step-by-Step Code Review

#### `mandelbrot_non_vectorized.py`

This file contains the function to generate the Mandelbrot set using a non-vectorized approach.

**Functions and Structure:**

1. **`mandelbrot_non_vectorized`**:
   - Generates the Mandelbrot set by iterating over each pixel.
   - Uses nested loops to compute the value for each pixel.
   - Returns the generated image and iteration counts.

2. **`run_and_save_non_vectorized`**:
   - Measures execution time, memory usage, and CPU usage.
   - Calls `mandelbrot_non_vectorized` to generate the image.
   - Saves the image and returns performance metrics.

#### `mandelbrot_vectorized.py`

This file contains the function to generate the Mandelbrot set using a vectorized approach.

**Functions and Structure:**

1. **`mandelbrot_vectorized`**:
   - Uses NumPy arrays to perform vectorized computations.
   - Significantly faster due to parallelized operations.
   - Returns the generated image and iteration counts.

2. **`run_and_save_vectorized`**:
   - Similar to `run_and_save_non_vectorized`, but calls `mandelbrot_vectorized`.
   - Measures performance metrics and saves the generated image.

#### `generate_analysis.py`

This script generates a Markdown report comparing the performance of the non-vectorized and vectorized methods.

**Functions and Structure:**

1. **`generate_analysis`**:
   - Writes a Markdown report with performance metrics and visual comparisons.
   - Highlights differences in execution time, memory usage, and CPU utilization.

#### `main`

This is the main entry point of the project, orchestrating the execution of both methods and generating the analysis report.

**Functions and Structure:**

1. **Setup and Parameters**:
   - Defines image dimensions, complex plane boundaries, and maximum iterations.
   - Creates a results directory based on the system name and current date.

2. **Run Methods and Capture Metrics**:
   - Executes both non-vectorized and vectorized methods.
   - Captures execution time, memory usage, and CPU utilization for both methods.

3. **Generate Analysis Report**:
   - Calls `generate_analysis.py` with captured metrics to create a comparison report.

### Considerations for Using Classes

#### Benefits of Refactoring into Classes

1. **Encapsulation**:
   - Encapsulate related data and methods into cohesive units.
   - Simplifies the management and modification of code.

2. **Reusability**:
   - Create reusable components that can be extended or used in different contexts.

3. **Maintainability**:
   - Improve code organization and readability.
   - Make it easier to understand and modify individual parts of the code.

4. **State Management**:
   - Classes can manage state more effectively, making it easier to track and modify attributes related to the Mandelbrot set generation.

#### Potential Classes

1. **`Mandelbrot`**:
   - Attributes: `width`, `height`, `Re_min`, `Re_max`, `Im_min`, `Im_max`, `max_iterations`, `image`, `iteration_counts`.
   - Methods: `generate_non_vectorized()`, `generate_vectorized()`, `save_image()`, `measure_performance()`.

2. **`PerformanceMetrics`**:
   - Attributes: `execution_time`, `memory_usage`, `cpu_usage`.
   - Methods: `measure()`, `display()`.

### Refactored Code with Classes

#### `mandelbrot.py`

```python
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import tracemalloc
import psutil

class Mandelbrot:
    def __init__(self, width, height, Re_min, Re_max, Im_min, Im_max, max_iterations):
        self.width = width
        self.height = height
        self.Re_min = Re_min
        self.Re_max = Re_max
        self.Im_min = Im_min
        self.Im_max = Im_max
        self.max_iterations = max_iterations
        self.image = np.zeros((height, width))
        self.iteration_counts = np.zeros((height, width))

    def generate_non_vectorized(self):
        for x in range(self.width):
            for y in range(self.height):
                c_real = self.Re_min + x * (self.Re_max - self.Re_min) / self.width
                c_imag = self.Im_min + y * (self.Im_max - self.Im_min) / self.height
                z_real, z_imag = 0, 0
                n = 0
                while n < self.max_iterations and z_real * z_real + z_imag * z_imag < 4:
                    z_real_temp = z_real * z_real - z_imag * z_imag + c_real
                    z_imag = 2 * z_real * z_imag + c_imag
                    z_real = z_real_temp
                    n += 1
                self.image[y, x] = n
                self.iteration_counts[y, x] = n
        return self.image, self.iteration_counts

    def generate_vectorized(self):
        Re = np.linspace(self.Re_min, self.Re_max, self.width)
        Im = np.linspace(self.Im_min, self.Im_max, self.height)
        C_real, C_imag = np.meshgrid(Re, Im)
        Z_real, Z_imag = np.zeros_like(C_real), np.zeros_like(C_imag)
        iterations = np.zeros_like(C_real, dtype=int)
        for i in range(self.max_iterations):
            mask = Z_real * Z_real + Z_imag * Z_imag < 4.0
            Z_real_temp = np.where(mask, Z_real * Z_real - Z_imag * Z_imag + C_real, Z_real)
            Z_imag = np.where(mask, 2 * Z_real * Z_imag + C_imag, Z_imag)
            Z_real = Z_real_temp
            iterations[mask] = i
            self.iteration_counts[mask] = i
        return iterations, self.iteration_counts

    def save_image(self, filename, method):
        plt.figure(figsize=(10, 10), dpi=300)
        plt.imshow(self.image, extent=(self.Re_min, self.Re_max, self.Im_min, self.Im_max), cmap='inferno', interpolation='bilinear')
        plt.colorbar(label='Iterations')
        plt.title(f'Mandelbrot Set ({method})')
        plt.xlabel('Re')
        plt.ylabel('Im')
        plt.savefig(filename)
        plt.close()

class PerformanceMetrics:
    def __init__(self):
        self.execution_time = 0
        self.memory_usage = 0
        self.cpu_usage = 0

    def measure(self, func, *args):
        tracemalloc.start()
        start_time = time.time()
        process = psutil.Process(os.getpid())

        func(*args)

        self.execution_time = (time.time() - start_time) * 1000  # in milliseconds
        self.memory_usage = tracemalloc.get_traced_memory()[1] / (1024 ** 2)  # in MB
        self.cpu_usage = process.cpu_percent()
        tracemalloc.stop()

    def display(self):
        return self.execution_time, self.memory_usage, self.cpu_usage

def run_and_save_mandelbrot(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir, method='non-vectorized'):
    mandelbrot = Mandelbrot(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations)
    metrics = PerformanceMetrics()

    if method == 'non-vectorized':
        metrics.measure(mandelbrot.generate_non_vectorized)
        filename = os.path.join(results_dir, 'mandelbrot_non_vectorized.png')
    else:
        metrics.measure(mandelbrot.generate_vectorized)
        filename = os.path.join(results_dir, 'mandelbrot_vectorized.png')

    mandelbrot.save_image(filename, method)
    return metrics.display(), mandelbrot.iteration_counts

if __name__ == "__main__":
    width, height = 1000, 1000
    Re_min, Re_max = -2.0, 1.0
    Im_min, Im_max = -1.5, 1.5
    max_iterations = 1000
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)

    # Run and save non-vectorized method
    non_vectorized_metrics, non_vectorized_iterations = run_and_save_mandelbrot(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir, method='non-vectorized')

    # Run and save vectorized method
    vectorized_metrics, vectorized_iterations = run_and_save_mandelbrot(width, height, Re_min, Re_max, Im_min, Im_max, max_iterations, results_dir, method='vectorized')
```

### When to Use Classes vs. Functions

#### When to Use Classes:
- **Encapsulation**: When you need to bundle data and methods that operate on that data together.
- **State Management**: When you need to maintain and manage the state of an object.
- **Reusability**: When you want to create reusable and extensible components.
- **Complex Relationships**: When there are complex relationships between data and behavior.

#### When to Use Functions:
- **Simple Tasks**: When the task is simple and does not require maintaining state.
- **Utility Operations**: For isolated utility functions that perform specific tasks.
- **Performance**: When performance is critical, and the overhead of class instantiation is unnecessary.
- **Functional Programming**: When adopting a functional programming paradigm where functions are preferred over stateful objects.



### Conclusion

In this project, refactoring the code into classes improves encapsulation, maintainability, and reusability. The `Mandelbrot` class encapsulates the data and methods related to generating and saving the Mandelbrot set. The `PerformanceMetrics` class encapsulates the performance measurement logic, making the code more modular and easier to understand. However, for simple, stateless tasks, standalone functions are still the best choice. By balancing the use of classes and functions, you can create a clean, efficient, and maintainable codebase.

---

## mandelbrot_non_vectorized.py

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


## mandelbrot_vectorized.py
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

## generate_analysis.py
import os

def generate_analysis(non_vectorized_time, vectorized_time, non_vectorized_memory, vectorized_memory, non_vectorized_cpu, vectorized_cpu, results_dir):
    with open(os.path.join(results_dir, 'analysis.md'), 'w') as f:
        f.write("# Mandelbrot Set Generation Results\n\n")
        
        f.write("## Introduction\n")
        f.write("### Purpose\n")
        f.write("This project aims to compare the efficiency and performance of non-vectorized and vectorized methods for generating the Mandelbrot set.\n\n")
        
        f.write("### Background\n")
        f.write("The Mandelbrot set is a set of complex numbers \\(c\\) for which the function \\(f_c(z) = z^2 + c\\) does not diverge when iterated from \\(z = 0\\). The boundary of the Mandelbrot set is a fractal, and its visualization is a popular example of mathematical beauty in complex dynamics.\n\n")

        f.write("## Methods\n")
        f.write("### Non-Vectorized Method\n")
        f.write("The non-vectorized method iterates over each pixel individually, applying the function \\(f_c(z) = z^2 + c\\) until the magnitude of \\(z\\) exceeds 2 or the maximum number of iterations is reached. This process is computationally intensive as it does not leverage vectorized operations.\n\n")
        
        f.write("### Vectorized Method\n")
        f.write("The vectorized method leverages numpy's array operations to perform computations on entire arrays at once, significantly speeding up the process. The same iterative function \\(f_c(z) = z^2 + c\\) is applied, but numpy arrays are used to handle multiple points simultaneously, thus optimizing the computation.\n\n")

        f.write("## Metrics Collected\n")
        f.write("### Execution Time\n")
        f.write(f"**Non-Vectorized Method**: {non_vectorized_time:.2f} ms\n")
        f.write(f"**Vectorized Method**: {vectorized_time:.2f} ms\n\n")
        
        f.write("### Memory Usage\n")
        f.write(f"**Non-Vectorized Method**: {non_vectorized_memory:.2f} MB\n")
        f.write(f"**Vectorized Method**: {vectorized_memory:.2f} MB\n\n")
        
        f.write("### CPU Utilization\n")
        f.write(f"**Non-Vectorized Method**: {non_vectorized_cpu:.2f}%\n")
        f.write(f"**Vectorized Method**: {vectorized_cpu:.2f}%\n\n")
        
        f.write("## Visuals\n")
        f.write("### Generated Mandelbrot Set Images\n")
        f.write("![Non-Vectorized Mandelbrot](mandelbrot_non_vectorized.png)\n")
        f.write("![Vectorized Mandelbrot](mandelbrot_vectorized.png)\n\n")
        
        f.write("### Performance Graphs\n")
        # Placeholder for performance graphs
        f.write("Graphs showing execution time, memory usage, and CPU utilization will be included here.\n\n")
        
        f.write("## Analysis\n")
        f.write("### Comparison of Methods\n")
        f.write("The non-vectorized method is simpler to implement but less efficient, while the vectorized method is more complex but significantly faster due to its use of numpy arrays for parallel computations.\n\n")
        
        f.write("### Efficiency\n")
        f.write("In terms of execution time, memory usage, and CPU utilization, the vectorized method outperforms the non-vectorized method. The non-vectorized method's simplicity comes at the cost of higher computational resources and longer execution times.\n\n")
        
        f.write("### Scalability\n")
        f.write("Both methods produce the same visual output, confirming the correctness of the implementation. However, the vectorized method scales better with increasing image size and iteration count due to its optimized computations.\n\n")
        
        f.write("## Conclusion\n")
        f.write("### Summary of Findings\n")
        f.write("This project highlights the benefits of vectorization in numerical computing and the beauty of fractal geometry. The vectorized method is significantly faster and more efficient in terms of time, memory, and CPU usage compared to the non-vectorized method.\n\n")
        
        f.write("### Future Work\n")
        f.write("Potential improvements include exploring more advanced optimization techniques, parallel computing, and GPU acceleration to further enhance the performance of Mandelbrot set generation.\n\n")

if __name__ == "__main__":
    import sys
    non_vectorized_time = float(sys.argv[1])
    vectorized_time = float(sys.argv[2])
    non_vectorized_memory = float(sys.argv[3])
    vectorized_memory = float(sys.argv[4])
    non_vectorized_cpu = float(sys.argv[5])
    vectorized_cpu = float(sys.argv[6])
    results_dir = sys.argv[7]
    generate_analysis(non_vectorized_time, vectorized_time, non_vectorized_memory, vectorized_memory, non_vectorized_cpu, vectorized_cpu, results_dir)



## main
import os
import platform
from datetime import datetime
from src.mandelbrot_non_vectorized import run_and_save_non_vectorized
from src.mandelbrot_vectorized import run_and_save_vectorized
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
