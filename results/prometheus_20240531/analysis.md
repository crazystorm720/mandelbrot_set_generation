# Mandelbrot Set Generation Results

## Non-Vectorized Method
![Non-Vectorized Mandelbrot](results/prometheus_20240531/mandelbrot_non_vectorized.png)
Execution time: 16201.86 ms
The non-vectorized method iterates over each pixel individually, which can be slow for large images.

## Vectorized Method
![Vectorized Mandelbrot](results/prometheus_20240531/mandelbrot_vectorized.png)
Execution time: 7324.07 ms
The vectorized method leverages numpy's array operations to perform computations on entire arrays at once, significantly speeding up the process.
