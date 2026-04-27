import multiprocessing

def sum_of_squares(numbers):
    return sum(n * n for n in numbers)

if __name__ == "__main__":
    data = list(range(1, 21))

    chunk_size = 5
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.map(sum_of_squares, chunks)

    total = sum(results)

    print("Chunks:", chunks)
    print("Partial results:", results)
    print("Final sum of squares:", total)