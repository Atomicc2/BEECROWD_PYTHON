def main():
    print('-' * 39)
    print('| decimal   |  octal  |  Hexadecimal  |')
    print('-' * 39)

    for i in range(16):
        dec = f'{i}'
        octal = f'{i:o}'
        hexa = f'{i:X}'
        print(f'| {dec:^9} | {octal:^7} | {hexa:^14}|')

    print('-' * 39)

if __name__ == '__main__':
    main()
