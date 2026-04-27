import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def linear_search(elements: list[int], target: int) -> bool:
    for element in elements:
        if target == element:
            return True

    return False

def binary_search(elements: set[int] | list[int], target: int) -> bool:
    ordered_list = sorted(elements)

    while ordered_list:
        index = len(ordered_list) // 2
        number = ordered_list[index]

        if number == target:
            return True
        elif target > number:
            ordered_list = ordered_list[index + 1:]
            continue
        ordered_list = ordered_list[:index]

    return False


def fibonacci(total_elements: int) -> int:
    if total_elements < 0:
        raise ValueError("total_elements must be non-negative")

    if total_elements == 0:
        return 0
    if total_elements == 1:
        return 1

    previous, current = 0, 1
    for _ in range(2, total_elements + 1):
        previous, current = current, previous + current

    return current
      

def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("number must be non-negative")

    if number <= 1:
        return 1
    return number * factorial(number - 1)
    

if __name__ == "__main__":
    lst_el = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

    for el in lst_el:
        start_time = time.perf_counter()
        elements = list(range(el))
        target = el - 1
        result = linear_search(elements, target)
        end_time = time.perf_counter()
        logger.info(f"Linear search for {el} elements: {result} (Time taken: {end_time - start_time:.6f} seconds)")
        print(factorial(856))