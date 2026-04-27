"""Count primes with threads.
 
- On `python3.14`  : GIL in effect → roughly sequential speed.
- On `python3.14t` : free-threaded → actually parallel.
 
Run the same file both ways to see the difference:
 
    uv run --python 3.14  main.py
    uv run --python 3.14t main.py
"""

from concurrent.futures import ThreadPoolExecutor
import math
import sys
import sysconfig
import time


def count_primes(limit: int) -> int:
    """"Count the number of prime numbers less than `limit`."""
    return sum(
        1
        for number in range(2, limit)
        if all(number % divisor for divisor in range(2, int(math.sqrt(number)) + 1))
    )


if __name__ == "__main__":
    free_threaded = bool(sysconfig.get_config_var("Py_GIL_DISABLED"))
    label = "3.14t (no-GIL)" if free_threaded else f"{sys.version_info.major}.{sys.version_info.minor} (GIL)"

    ranges = [2_000_000] * 8

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as executor:
        total = sum(executor.map(count_primes, ranges))
    dt = time.perf_counter() - t0

    print(f"Python {label}  Threads(8):  {dt:5.2f}s Total Primes: {total}")