def reverse_string(string):
    reversed = ''
    for i in range(len(string) - 1, -1, -1):
        reversed += string[i]
    return reversed


if __name__ == '__main__':
    string = input('Enter a string: ')
    print(f'Reversed string: {reverse_string(string)}')
