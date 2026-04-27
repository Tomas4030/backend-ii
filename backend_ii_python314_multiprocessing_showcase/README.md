# backend_ii_python314_multiprocessing_showcase

Showcase of Python 3.14 multiprocessing and threading for CPU-bound and I/O-bound tasks.

## Overview

This project demonstrates:

- **Multiprocessing for CPU-bound tasks**: Counting prime numbers in a large range using multiple processes.
- **Threading for I/O-bound tasks**: Fetching multiple URLs concurrently using threads.

## Scripts

- `processes_cpu.py`: Uses `ProcessPoolExecutor` to count primes in parallel. Demonstrates how to split a large computation into chunks and process them across multiple CPU cores.
- `threads_cpu.py`: Uses `ThreadPoolExecutor` to fetch several URLs concurrently. Demonstrates how threads can speed up I/O-bound operations.

## Usage

You can run the scripts individually or together using the provided `Makefile`:

```sh
# Run both scripts (setup, then threads, then processes)
make run.all

# Run only the threading example
make run.threads_cpu

# Run only the multiprocessing example
make run.processes_cpu
```

## Requirements

- Python 3.14.4 (managed via [uv](https://github.com/astral-sh/uv) and pinned in the Makefile)

## Project Structure

- `main.py`: Entry point (prints a hello message).
- `processes_cpu.py`: Multiprocessing showcase (CPU-bound).
- `threads_cpu.py`: Threading showcase (I/O-bound).
- `Makefile`: Setup and run commands.
- `pyproject.toml`: Project metadata.

## Notes

- Multiprocessing is used for CPU-bound tasks to bypass the GIL and utilize multiple cores.
- Threading is used for I/O-bound tasks to overlap waiting times.

---
For more details, see the code and comments in each script.