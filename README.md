# COMP 211 Checkoff 3 - How Python Libraries Are Implemented in C

## Overview

Python is one of the most widely used programming languages in machine learning, despite being relatively slow at executing certain operations compared to compiled languages like C.

This project explores how Python interacts with C, how libraries like NumPy leverage compiled code, and why this architecture makes Python so powerful for scientific computing.

Link to my presentation slides: [COMP 211 Checkoff 3 Presentation Slides](https://docs.google.com/presentation/d/1UqhsyJJ6wQdAbIPiwqbyez8vOPOAcKrAJqUBvn4Kx6s/edit?usp=sharing)

## What I Explored

### 1. Calling C from Python

I experimented with Python's built-in `ctypes` library to call a function written in C.

The process involves:

1. Writing a C function to perform a computation.
2. Compiling it into a shared library (`.so`) using GCC.
3. Loading the library in Python using `ctypes.CDLL()`.
4. Calling the C function and accessing the results in Python.

### 2. C Extensions vs. ctypes

I explored two ways Python can interact with compiled C code:

- **ctypes:** Allows Python to call functions from existing C shared libraries.
- **C Extensions:** Allow developers to create Python-importable modules using C and the Python/C API.

Libraries like NumPy use compiled extension modules to implement many performance-critical operations.

### 3. NumPy and Performance

I investigated why NumPy can process large numerical arrays more efficiently than ordinary Python loops.

Unlike Python lists, standard numerical NumPy arrays store homogeneous values in compact memory buffers, allowing compiled code to process data efficiently.

I also created a benchmark comparing Python list comprehensions and NumPy operations across different array sizes to visualize their performance differences.

## Running the Examples

**Requirements:** Python 3, GCC (Linux), NumPy, and Matplotlib.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib jupyter
```

Compile the C example:

```bash
gcc -shared -fPIC double.c -o libdouble.so
```

Run the Python example:

```bash
python double.py
```

For the performance experiment, open the performance.py in VS Code or run:

```bash
python performance.py
```

## Key Takeaways

- Python can delegate computationally expensive operations to compiled languages like C.
- NumPy's performance comes from both efficient memory representation and compiled numerical operations.
- High-level programming languages can combine ease of use with the performance of lower-level implementations.

## Additional Resources

- [Python ctypes Documentation](https://docs.python.org/3/library/ctypes.html)
- [Python/C API Reference](https://docs.python.org/3/c-api/index.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy Internals](https://numpy.org/doc/stable/dev/internals.html)