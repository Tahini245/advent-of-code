def main(input: str) -> int:
    coords = [complex(), complex()]
    houses = {complex()}
    for i, instruction in enumerate(input):
        moving = i % 2
        x = coords[moving].real
        y = coords[moving].imag
        match instruction:
            case '^':
                coords[moving] = complex(x, y + 1)
            case 'v':
                coords[moving] = complex(x, y - 1)
            case '>':
                coords[moving] = complex(x + 1, y)
            case '<':
                coords[moving] = complex(x - 1, y)
        houses.add(coords[moving])
    return len(houses)


if __name__ == '__main__':
    with open('2015/3/input.txt') as file:
        print(main(file.read()), 'houses receive at least one present')
