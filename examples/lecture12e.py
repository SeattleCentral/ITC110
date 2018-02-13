from tkinter.filedialog import askopenfilename, asksaveasfilename


def show_content():
    filename = input('Enter a filename to view its content: ')
    file = open(filename, 'r')

    for line in file:
        print(line)

    file.close()

# show_content()


def write_diary():
    filename = input('Enter diary journal name: ')
    file = open(filename, 'w')
    journal_entry = ''

    while journal_entry != 'X':
        journal_entry = input('Enter note, or type "X" to exit: ')
        print(journal_entry, file=file)

    file.close()

# write_diary()


def batch_processing():
    print('Process temperature records.')

    input_filename = askopenfilename()
    output_filename = asksaveasfilename()

    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    temp_sum = 0.0
    temp_count = 0

    for line in input_file:
        content_list = line.split(',')
        try:
            for temp in content_list:
                temp_sum = temp_sum + float(temp)
                temp_count += 1
        except ValueError:
            continue

    input_file.close()
    avg_temp = temp_sum / temp_count
    print("The average temp. is: {0}ºF".format(avg_temp), file=output_file)
    output_file.close()
    return avg_temp


print("The average temp. is: {0}ºF".format(batch_processing()))



