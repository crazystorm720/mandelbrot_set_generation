# Mandelbrot Set Generation

This project demonstrates the generation of the Mandelbrot set using both non-vectorized and vectorized approaches. It provides a comprehensive comparison of the performance and execution times of these two methods. The generated images and execution metrics are documented in a Markdown report.

## Project Structure

```
MyProject/
├── .gitignore
├── my_project_env/
├── environment.yml
├── requirements.txt
├── src/
│   ├── generate_analysis.py
│   ├── main.py
│   ├── mandelbrot_non_vectorized.py
│   ├── mandelbrot_vectorized.py
└── tests/
```

## Setup and Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/MyProject.git
    cd MyProject
    ```

2. **Create and activate the conda environment:**
    ```sh
    conda env create -f environment.yml
    conda activate mandelbrot
    ```

3. **Install the Python dependencies using pip:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main script to generate the Mandelbrot sets and the analysis report:**
    ```sh
    python src/main.py
    ```

## Scripts Overview

### src/mandelbrot_non_vectorized.py

This script contains the function `mandelbrot_non_vectorized` which generates the Mandelbrot set using a nested loop approach to iterate over each pixel. The execution time is measured and the resulting image is saved as `mandelbrot_non_vectorized.png`.

### src/mandelbrot_vectorized.py

This script contains the function `mandelbrot_vectorized` which leverages numpy's vectorized operations to perform computations on entire arrays at once. The execution time is measured and the resulting image is saved as `mandelbrot_vectorized.png`.

### src/generate_analysis.py

This script generates a Markdown report (`analysis.md`) that documents the execution times and provides a detailed comparison between the non-vectorized and vectorized methods. It includes mathematical explanations and visual outputs of the Mandelbrot sets.

### src/main.py

The main script orchestrates the execution of both the non-vectorized and vectorized scripts, captures the execution times, and calls the `generate_analysis.py` script to create the analysis report.

## Results

After running the main script, a new directory will be created under `results/` named with the system name and current date (down to the minute). This directory will include:

- `mandelbrot_non_vectorized.png`: Image of the Mandelbrot set generated using the non-vectorized method.
- `mandelbrot_vectorized.png`: Image of the Mandelbrot set generated using the vectorized method.
- `analysis.md`: Markdown report detailing the execution times and providing a comparison of the two methods.

### Example Structure

```
results/
└── prometheus_20240531_1345/
    ├── analysis.md
    ├── mandelbrot_non_vectorized.png
    └── mandelbrot_vectorized.png
```

This setup ensures that each run's results are well-organized and easily traceable.

---

### environment.yml

```yaml
name: mandelbrot
channels:
  - defaults
dependencies:
  - python=3.11
  - pip
  - pip:
    - -r requirements.txt
```

### requirements.txt

```txt
numpy
matplotlib
psutil
```
