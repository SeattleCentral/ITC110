def main():
    filename = input('Enter a filename: ')
    infile = open(filename, 'r')
    data = infile.read()
    # Interrupt for a moment.
    input('Ready to print?')
    print(data)

    file.close()


main()


# Not part of the class
# FYI only
def othermain():
    filename = 'nsa_notes.txt'

    # Safer way to open a file.
    with open(filename, 'r') as file:
        file.read()


othermain()
