# Encoding characters

def encoder(message):
    print("ITC 110's fancy encryption app.")

    encrypted = ""

    for character in message:
        encrypted = encrypted + str(ord(character)) + " "

    # Removes the final space character
    encrypted = encrypted[:-1]

    return encrypted

def decoder(secret):
    # Secret is a string of numbers separated by a space.
    # E.g. "66 111 98 98 121"
    print("Hold on while I decrypt your message...")

    # message = ""
    message = []

    # Should create a list of characters
    # E.g. ["66", "111", "98", "98", "121"]
    code_list = secret.split(" ")

    for code in code_list:
        # message = message + chr(int(code))
        message.append(chr(int(code)))

    # Now message is a List
    # ['a', 'b', 'c'] => 'abc'
    message = ''.join(message)

    return message



def main():
    message = input("What's you secret message? ")

    secret = encoder(message)

    print("The secret is:")
    print(secret)

    decoded_message = decoder(secret)

    print("The decoded message is:")
    print(decoded_message)


main()







