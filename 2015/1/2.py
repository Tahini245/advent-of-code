def main() -> int:
    with open('input.txt') as file:
        floor = 0
        for i, instruction in enumerate(file.read()):
            if instruction == '(':
                floor += 1
            else:
                floor -= 1
                if floor < 0:
                    return i + 1


if __name__ == '__main__':
    print(f'Santa first enters the basement at char no. {main()}')
