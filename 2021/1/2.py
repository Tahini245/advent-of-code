def main(input: str) -> int:
    sum = first = second = 0
    increases = -3
    for cur in map(int, input.splitlines()):
        if first + second + cur > sum:
            increases += 1
        sum = first + second + cur
        first, second = second, cur
    return increases


if __name__ == "__main__":
    with open("2021/1/input.txt") as file:
        print(main(file.read()), "sums are larger than the previous one")
