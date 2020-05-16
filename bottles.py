grouper = lambda n: 'bottles' if n != 1 else 'bottle'

# Recursively
def print_bottles(count):
    counter = grouper(count)
    next_count = count - 1

    print(f'{count} {counter} of beer on the wall, {count} {counter} of beer.')

    # base
    if next_count == 0:
        print('Go to the store and buy some more, 99 bottles of beer on the wall.')
        return

    print(f'Take one down and pass it around, {next_count} {grouper(next_count)} of beer on the wall.\n')
    print_bottles(next_count)


# Iteratively
def print_bottles2(start):
    for bottle in [(n, n - 1) for n in range(start, 0, -1)]:
        count, next_count = bottle
        counter = grouper(count)
        next_counter = grouper(next_count)

        print(f'{count} {counter} of beer on the wall, {count} {counter} of beer.')

        if next_count > 0:
            print(f'Take one down and pass it around, {next_count} {next_counter} of beer on the wall.\n')
        else:
            print('Go to the store and buy some more, 99 bottles of beer on the wall.')
