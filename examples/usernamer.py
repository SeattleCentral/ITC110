# Madenning Username Generator
# Returns first char of first name and first 7 chars of last name


def usernamer(first_name, last_name):
    username = first_name[0] + last_name[:7]
    return username.lower()


if __name__ == '__main__':
    # Testing
    assert usernamer("Joshua", "Wedekind") == "jwedekin"


    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")


    print(usernamer(first_name, last_name))

