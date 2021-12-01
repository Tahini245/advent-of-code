def main(input: str) -> int:
    prev = 0
    increases = -1
    for cur in map(int, input.splitlines()):
        if cur > prev:
            increases += 1
        prev = cur
    return increases


if __name__ == "__main__":
    with open("2021/1/input.txt") as file:
        print(main(file.read()), "measurements are larger than the previous one")
