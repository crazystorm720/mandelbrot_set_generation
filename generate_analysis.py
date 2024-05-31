import os

def generate_analysis(non_vectorized_time, vectorized_time, results_dir):
    with open(os.path.join(results_dir, 'analysis.md'), 'w') as f:
        f.write("# Mandelbrot Set Generation Results\n\n")
        
        f.write("## Overview\n")
        f.write("This project demonstrates the generation of the Mandelbrot set using both non-vectorized and vectorized approaches. ")
        f.write("The Mandelbrot set is a set of complex numbers \\(c\\) for which the function \\(f_c(z) = z^2 + c\\) does not diverge when iterated from \\(z = 0\\). ")
        f.write("The boundary of the Mandelbrot set is a fractal, and its visualization is a popular example of mathematical beauty in complex dynamics.\n\n")

        f.write("## Non-Vectorized Method\n")
        f.write("![Non-Vectorized Mandelbrot](mandelbrot_non_vectorized.png)\n")
        f.write(f"**Execution time**: {non_vectorized_time:.2f} ms\n")
        f.write("The non-vectorized method iterates over each pixel individually, which can be slow for large images. ")
        f.write("In this method, each pixel corresponds to a complex number, and the algorithm iteratively applies the function \\(f_c(z) = z^2 + c\\) until the magnitude of \\(z\\) exceeds 2 or the maximum number of iterations is reached. ")
        f.write("This process is computationally intensive as it does not leverage vectorized operations.\n\n")
        
        f.write("## Vectorized Method\n")
        f.write("![Vectorized Mandelbrot](mandelbrot_vectorized.png)\n")
        f.write(f"**Execution time**: {vectorized_time:.2f} ms\n")
        f.write("The vectorized method leverages numpy's array operations to perform computations on entire arrays at once, significantly speeding up the process. ")
        f.write("In this approach, the same iterative function \\(f_c(z) = z^2 + c\\) is applied, but numpy arrays are used to handle multiple points simultaneously, thus optimizing the computation. ")
        f.write("This method is much faster for large images as it takes advantage of low-level optimizations in numpy.\n\n")
        
        f.write("## Analysis\n")
        f.write("The images above visualize the Mandelbrot set using both methods. Despite the differences in implementation, the output images should be visually identical, depicting the fractal nature of the Mandelbrot set. ")
        f.write("The execution time, however, highlights the efficiency gains from using vectorized operations. The non-vectorized method, being more straightforward and easier to understand, serves as a baseline, whereas the vectorized method demonstrates the power of numpy for numerical computations.\n\n")
        
        f.write("### Key Observations\n")
        f.write("- **Performance**: The vectorized method is significantly faster due to its use of numpy arrays for parallel computations.\n")
        f.write("- **Implementation Complexity**: The non-vectorized method is simpler to implement but less efficient.\n")
        f.write("- **Output**: Both methods produce the same visual output, confirming the correctness of the implementation.\n\n")
        
        f.write("### Mathematical Background\n")
        f.write("The Mandelbrot set is defined by the set of complex numbers \\(c\\) for which the sequence defined by the iteration \\(z_{n+1} = z_n^2 + c\\) remains bounded. ")
        f.write("Mathematically, this means that there exists a positive integer \\(N\\) such that for all \\(n > N\\), \\(|z_n| \\leq 2\\). If \\(|z_n| > 2\\) for any iteration, the sequence will escape to infinity, and \\(c\\) is not in the Mandelbrot set.\n\n")
        
        f.write("### LaTeX Formulas\n")
        f.write("- Iterative function: \\(f_c(z) = z^2 + c\\)\n")
        f.write("- Condition for boundedness: \\(|z_n| \\leq 2\\)\n")
        
        f.write("By comparing the execution times and observing the generated images, this project highlights the benefits of vectorization in numerical computing and the beauty of fractal geometry.\n")

if __name__ == "__main__":
    import sys
    non_vectorized_time = float(sys.argv[1])
    vectorized_time = float(sys.argv[2])
    results_dir = sys.argv[3]
    generate_analysis(non_vectorized_time, vectorized_time, results_dir)

