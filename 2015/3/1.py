def main(filename: str) -> int:
    with open(filename) as file:
        coords = complex()
        houses = {coords}
        for i in file.read():
            x = coords.real
            y = coords.imag
            match i:
                case '^':
                    coords = complex(x, y + 1)
                case 'v':
                    coords = complex(x, y - 1)
                case '>':
                    coords = complex(x + 1, y)
                case '<':
                    coords = complex(x - 1, y)
            houses.add(coords)
    return len(houses)


if __name__ == '__main__':
    print(main('input.txt'), 'houses receive at least one present')
