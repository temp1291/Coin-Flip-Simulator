from random import randint


def main():
    while True:
        input('Press Enter to flip a coin...')
        result = flip_coin()
        print(result)


def flip_coin():
    result = randint(0, 1)
    if result:
        return 'It landed heads.\n'
    else:
        return 'It landed tails.\n'


if __name__ == '__main__':
    main()
