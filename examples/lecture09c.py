secret_message = input('Enter a secret message: ')
encoded_message = ''
list_encoded_message = []

for character in secret_message:
    # encoded_message += str(ord(character)) + '-'
    # e.g. 76-92-42-31-
    list_encoded_message.append(ord(character))
    # e.g. [76, 92, 42, 31, ]

# encoded_message = encoded_message[:-1]
# e.g. 76-92-42-31

# print('Encoded message:', encoded_message)
print ('Encoded list: ', list_encoded_message)


decoded_message = ''
list_decoded_message = []

for encoded_char in list_encoded_message:
    print(encoded_char)
    list_decoded_message.append(chr(encoded_char))
    # ['H', 'e', 'l', 'l', 'o', ]

print ('Decoded list: ', list_decoded_message)

decoded_message = ''.join(list_decoded_message)

print('The decoded message:', decoded_message)
