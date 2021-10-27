from hashlib import md5


def main(input: str) -> int:
    x = 1
    while not md5((input + str(x)).encode()).hexdigest().startswith('00000'):
        x += 1
    return x


if __name__ == '__main__':
    print('The lowest number to produce such a hash is', main('ckczppom'))
