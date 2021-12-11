from math import prod


def main(input: str) -> int:
    total = 0
    for present in input.splitlines():
        dimensions = l, w, h = [int(x) for x in present.split("x")]
        total += 2 * (l * w + w * h + h * l)
        dimensions.remove(max(dimensions))
        total += prod(dimensions)
    return total


if __name__ == "__main__":
    with open("2015/2/input.txt") as file:
        print(
            f"The elves should order {main(file.read())} square feet of wrapping paper"
        )
