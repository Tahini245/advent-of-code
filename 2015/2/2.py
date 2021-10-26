from math import prod


def main(input: str) -> int:
    total = 0
    for present in input.splitlines():
        dimensions = [int(x) for x in present.split('x')]
        total += prod(dimensions)
        dimensions.remove(max(dimensions))
        total += 2 * sum(dimensions)
    return total


if __name__ == '__main__':
    with open('2015/2/input.txt') as file:
        print(f'The elves should order {main(file.read())} feet of ribbon')
