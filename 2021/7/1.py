from statistics import median


def main(input: str):
    crabs = [int(crab) for crab in input.split(',')]
    pos = median(crabs)
    return sum(abs(pos - crab) for crab in crabs)


if __name__ == '__main__':
    with open('2021/7/7.in') as f:
        print(main(f.read()), 'fuel must be used')
