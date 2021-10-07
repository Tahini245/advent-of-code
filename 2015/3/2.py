def main(filename: str) -> int:
    with open(filename) as file:
        santa = [0, 0]
        robo = [0, 0]
        houses = {tuple(santa)}
        for i, instruction in enumerate(file.read()):
            moving = robo if i % 2 else santa
            match instruction:
                case '^':
                    moving[1] += 1
                case 'v':
                    moving[1] -= 1
                case '>':
                    moving[0] += 1
                case '<':
                    moving[0] -= 1
            houses.add(tuple(moving))
    return len(houses)


if __name__ == '__main__':
    print(main('input.txt'), 'houses receive at least one present')
