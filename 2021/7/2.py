from functools import lru_cache
from math import ceil, floor
from statistics import mean


@lru_cache(None)
def triangular(n: int):
    return n * (n + 1) / 2


def main(input: str):
    crabs = [int(crab) for crab in input.split(",")]
    average = mean(crabs)
    low = floor(average)
    high = ceil(average)
    return min(
        sum(triangular(abs(low - crab)) for crab in crabs),
        sum(triangular(abs(high - crab)) for crab in crabs),
    )


if __name__ == "__main__":
    with open("2021/7/7.in") as f:
        print(main(f.read()), "fuel must be used")
