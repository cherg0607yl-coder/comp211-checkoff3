import time
import statistics
import numpy as np
import matplotlib.pyplot as plt

# Different numbers of elements
sizes = [100, 1_000, 10_000, 100_000, 1_000_000, 5_000_000]

python_times = []
numpy_times = []

repeats = 7

for n in sizes:
    python_data = list(range(n))
    numpy_data = np.arange(n, dtype=np.int64)

    # Warm up both approaches
    [x * 2 for x in python_data[:100]]
    numpy_data * 2

    # Benchmark Python
    trials = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = [x * 2 for x in python_data]
        trials.append(time.perf_counter() - start)

    python_time = statistics.median(trials)

    # Benchmark NumPy
    trials = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = numpy_data * 2
        trials.append(time.perf_counter() - start)

    numpy_time = statistics.median(trials)

    python_times.append(python_time * 1000)
    numpy_times.append(numpy_time * 1000)

    print(
        f"n={n:>10,} | "
        f"Python={python_time * 1000:>9.3f} ms | "
        f"NumPy={numpy_time * 1000:>9.3f} ms | "
        f"Speedup={python_time / numpy_time:>7.1f}x"
    )

# Plot results
plt.figure(figsize=(10, 6))

plt.plot(sizes, python_times, marker="o", label="Python list comprehension")
plt.plot(sizes, numpy_times, marker="s", label="NumPy compiled operation")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (ms)")
plt.title("Python vs NumPy: Performance by Array Size")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("benchmark.png", dpi=300)
plt.show()