def main(input: str):
    CHAR_NO = {2, 3, 4, 7}
    outputs = (line.split("|")[1].split() for line in input.splitlines())
    return sum(sum(len(digit) in CHAR_NO for digit in output) for output in outputs)


if __name__ == "__main__":
    with open("2021/8/8.in") as f:
        print(f"The specified digits appear {main(f.read())} times")
