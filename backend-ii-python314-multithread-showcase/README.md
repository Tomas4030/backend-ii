
# backend-ii-python314-multithread-showcase

**Showcase: Python's GIL vs. Free-threaded Python for CPU-bound multithreading.**

This project demonstrates the impact of Python's Global Interpreter Lock (GIL) on multi-threaded CPU-bound workloads, using Python 3.14 and the experimental free-threaded build (3.14t).

---

## Requirements

- [uv](https://github.com/astral-sh/uv) (for Python version management and running)
- Python 3.10, 3.14, and/or 3.14t (free-threaded)

---

This project demonstrates the impact of Python's Global Interpreter Lock (GIL) on multi-threaded CPU-bound workloads, using Python 3.14 and the experimental free-threaded build (3.14t).


## Setup

Clone the repository and ensure you have `uv` installed. Then, run:

```
make setup
```

This will install Python 3.10, 3.14, and 3.14t (free-threaded) using uv.

No additional dependencies are required.

---

The script `main.py` counts the number of prime numbers below 2,000,000 using 8 threads. It highlights the difference in performance between:

- **Standard Python 3.14**: GIL is in effect, so threads run sequentially for CPU-bound tasks.
- **Python 3.14t (free-threaded)**: GIL is disabled, allowing true parallel execution of threads.

## Usage



You can run the benchmark with different Python versions using [uv](https://github.com/astral-sh/uv). A `Makefile` is provided for convenience. Before running, make sure to execute `make setup` at least once:


```
make run.3.10    # Run with Python 3.10
make run.3.14    # Run with Python 3.14 (GIL)
make run.314t    # Run with Python 3.14t (no GIL)
make run.all     # Run all above sequentially
```


Or run directly with uv:


```
uv run --python 3.14 main.py    # Standard Python 3.14
uv run --python 3.14t main.py   # Free-threaded Python 3.14t
```


---

## Output Example

The script prints the Python version, threading mode, elapsed time, and total primes found:

```
Python 3.14 (GIL)  Threads(8):  12.34s Total Primes: 1429836
Python 3.14t (no-GIL)  Threads(8):  2.56s Total Primes: 1429836
```


---

## License

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for details.