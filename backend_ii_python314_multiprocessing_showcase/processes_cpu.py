from concurrent.futures import ProcessPoolExecutor
import math
import multiprocessing
import time

"Arguments and return values are pickled across the process boundary, "
"so keep per-task payloads reasonable and "
"make each task large enough to justify the overhead."
"Pickling is Python's built-in serialization "
"— turning a live Python object "
"(a list, a dict, a NumPy array, a custom class instance) "
"into a stream of bytes that can be stored or sent somewhere, "
"and later turned back into an equivalent object. "
"The module is literally called pickle."

def is_prime(number:int)-> bool:
    """Returns True if the number is prime, False otherwise."""
    if number < 2: return False
    if number % 2 == 0: return number == 2
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True

def count_primes(bounds:tuple[int, int])-> int:
    """Returns the count of prime numbers within the given bounds."""
    start, end = bounds
    if start > end:
        raise ValueError("Start of bounds must be less than or equal to end.")
    return sum(1 for num in range(start, end + 1) if is_prime(num))


if __name__ == "__main__":
    multiprocessing.set_start_method("forkserver", force=True)
    N, chunk = 5_000_000, 500_000
    ranges = [(i, min(i+chunk,N)) for i in range(0,N,chunk)]

    t0 = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        results = sum(executor.map(count_primes, ranges))
    
    print(f"{results} primes below {N} in {time.perf_counter() - t0:.2f} seconds")