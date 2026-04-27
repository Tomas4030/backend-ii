from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen
from time import perf_counter

"Running sequentially, total time ≈ sum of each request. "
"With threads, total time ≈ the slowest single request."


URLS = [
    "https://www.python.org",
    "https://docs.python.org/3/",
    "https://pypi.org",
    "https://httpbin.org/delay/1",
]


def fetch(url: str) -> tuple[str, int]:
    with urlopen(url, timeout=10) as r:
        return url, len(r.read())


if __name__ == "__main__":
    t0 = perf_counter()
    with ThreadPoolExecutor(max_workers=8) as pool:
        for fut in as_completed(pool.submit(fetch, u) for u in URLS):
            url, size = fut.result()
            print(f"{size:>8} bytes  {url}")
    print(f"done in {perf_counter() - t0:.2f}s")
