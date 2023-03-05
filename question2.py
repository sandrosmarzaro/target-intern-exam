def is_fibonacci(number):
    if number < 0:
        return False
    elif number == 0 or number == 1:
        return True
    else:
        previous, current = 0, 1
        while current < number:
            previous, current = current, previous + current
        return current == number


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print(f'{number} is a fibonacci sequence number: {is_fibonacci(number)}')
