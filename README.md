# Mandelbrot Set Generation

This project demonstrates the generation of the Mandelbrot set using both non-vectorized and vectorized approaches. It provides a comprehensive comparison of the performance and execution times of these two methods. The generated images and execution metrics are documented in a Markdown report.

## Project Structure

```
mandelbrot/
├── environment.yml
├── main.py
├── mandelbrot_non_vectorized.py
├── mandelbrot_vectorized.py
├── __pycache__
│   ├── mandelbrot_non_vectorized.cpython-311.pyc
│   └── mandelbrot_vectorized.cpython-311.pyc
└── results/
    ├── {system_name_date}
    │   ├── analysis.md
    │   ├── mandelbrot_non_vectorized.png
    │   └── mandelbrot_vectorized.png
```

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

The main script orchestrates the execution of both the non-vector

ized and vectorized scripts. It captures the execution times, generates the Mandelbrot set images, and compiles a Markdown report (`analysis.md`) containing the results and performance comparison.

## Scripts Overview

### mandelbrot_non_vectorized.py

This script contains the function `mandelbrot_non_vectorized` which generates the Mandelbrot set using a nested loop approach to iterate over each pixel. The execution time is measured and the resulting image is saved as `mandelbrot_non_vectorized.png`.

### mandelbrot_vectorized.py

This script contains the function `mandelbrot_vectorized` which leverages numpy's vectorized operations to perform computations on entire arrays at once. The execution time is measured and the resulting image is saved as `mandelbrot_vectorized.png`.

### main.py

The main script orchestrates the execution of both the non-vectorized and vectorized scripts. It captures the execution times, generates the Mandelbrot set images, and compiles a Markdown report (`analysis.md`) containing the results and performance comparison.

## Results

The results directory will contain a subdirectory named `{system_name_date}` after running the main script. This subdirectory will include:

- `mandelbrot_non_vectorized.png`: Image of the Mandelbrot set generated using the non-vectorized method.
- `mandelbrot_vectorized.png`: Image of the Mandelbrot set generated using the vectorized method.
- `analysis.md`: Markdown report detailing the execution times and providing a comparison of the two methods.
