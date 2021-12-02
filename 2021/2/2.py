def main(input: str) -> float:
    aim = 0
    pos = 0j
    for instruction, amount in map(str.split, input.splitlines()):
        amount = int(amount)
        match instruction:
            case "forward":
                pos = complex(pos.real + amount, pos.imag + aim * amount)
            case "up":
                aim -= amount
            case "down":
                aim += amount
    return pos.real * pos.imag


if __name__ == "__main__":
    with open("2021/2/input.txt") as file:
        print(
            f"You get {main(file.read())} if you multiply your final horizontal position by your final depth"
        )
