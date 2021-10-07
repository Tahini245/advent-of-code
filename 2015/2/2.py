from math import prod


def main(filename: str) -> int:
    with open(filename) as file:
        total = 0
        for present in file.read().splitlines():
            dimensions = [int(x) for x in present.split('x')]
            total += prod(dimensions)
            dimensions.remove(max(dimensions))
            total += 2 * sum(dimensions)
    return total


if __name__ == '__main__':
    print(f'The elves should order {main("input.txt")} feet of ribbon')
