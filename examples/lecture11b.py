def main():
    # Batch processing NSA notes
    input_filename = 'nsa_notes.txt'
    output_filename = 'nsa_secrets.txt'

    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    trigger_terms = ['hack', 'bomb', 'bobm', 'classified',
                     'president', 'interrogate', 'bob',
                     'sally', 'atom', 'python', 'company',
                     'money', 'network', 'prism', 'code']

    for line in input_file.readlines():
        for term in trigger_terms:
            if term in line.lower():
                print(line, file=output_file)

    input_file.close()
    output_file.close()

main()
