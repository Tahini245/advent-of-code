def main() -> int:
    with open('input.txt') as file:
        total = 0
        for present in file.read().splitlines():
            dimensions = l, w, h = [int(x) for x in present.split('x')]
            total += 2 * (l * w + w * h + h * l)
            dimensions.remove(max(dimensions))
            total += dimensions[0] * dimensions[1]
        return total


if __name__ == '__main__':
    print(f'The elves should order {main()} square feet of wrapping paper')
