from tkinter.filedialog import askopenfilename

def main():
    sum = 0.0
    count = 0

    filename = askopenfilename()

    file = open(filename, 'r')

    header = file.readline()

    # for line in file.readlines():
    #     temp = float(line)
    #     sum += temp
    #     count += 1

    line = file.readline()
    while line != '':
        row = line.split(',')
        for column in row:
            try:
                temp = float(column)
                sum += temp
                count += 1
            except:
                print("Skipping invalid line.")
        line = file.readline()

    print("The average temperature is:", sum / count)


if __name__ == '__main__':
    print ("Get the average temperature.")
    main()
