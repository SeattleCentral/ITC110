def main():
    file = open('nsa_notes.txt', 'r')

    for line in file.readlines():
        if 'spy' in line:
            print(line)

    file.close()


main()
