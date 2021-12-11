def main(input: str) -> int:
    coords = complex()
    houses = {coords}
    for i in input:
        x = coords.real
        y = coords.imag
        match i:
            case "^":
                coords = complex(x, y + 1)
            case "v":
                coords = complex(x, y - 1)
            case ">":
                coords = complex(x + 1, y)
            case "<":
                coords = complex(x - 1, y)
        houses.add(coords)
    return len(houses)


if __name__ == "__main__":
    with open("2015/3/input.txt") as file:
        print(main(file.read()), "houses receive at least one present")
