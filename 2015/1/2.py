def main(input: str) -> int:  # type: ignore[return]
    floor = 0
    for i, instruction in enumerate(input):
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
            if floor < 0:
                return i + 1


if __name__ == '__main__':
    with open('2015/1/input.txt') as file:
        print('Santa first enters the basement at char no.', main(file.read()))
