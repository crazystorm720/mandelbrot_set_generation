
## Setup and Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/mandelbrot.git
    cd mandelbrot
    ```

2. **Create and activate the conda environment:**
    ```sh
    conda env create -f environment.yml
    conda activate mandelbrot
    ```

3. **Run the main script to generate the Mandelbrot sets and the analysis report:**
    ```sh
    python main.py
    ```

## Usage

The main script orchestrates the execution of both the non-vectorized and vectorized scripts. It captures the execution times, generates the Mandelbrot set images, and compiles a Markdown report (`analysis.md`) containing the results and performance comparison.

## Scripts Overview

### mandelbrot_non_vectorized.py

This script contains the function `mandelbrot_non_vectorized` which generates the Mandelbrot set using a nested loop approach to iterate over each pixel. The execution time is measured and the resulting image is saved as `mandelbrot_non_vectorized.png`.

### mandelbrot_vectorized.py

This script contains the function `mandelbrot_vectorized` which leverages numpy's vectorized operations to perform computations on entire arrays at once. The execution time is measured and the resulting image is saved as `mandelbrot_vectorized.png`.

### main.py

The main script orchestrates the execution of both the non-vectorized and vectorized scripts. It captures the execution times, generates the Mandelbrot set images, and compiles a Markdown report (`analysis.md`) containing the results and performance comparison.

## Results

The results directory will contain the following files after running the main script:

- `mandelbrot_non_vectorized.png`: Image of the Mandelbrot set generated using the non-vectorized method.
- `mandelbrot_vectorized.png`: Image of the Mandelbrot set generated using the vectorized method.
- `analysis.md`: Markdown report detailing the execution times and comparing the two methods.
