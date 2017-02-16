from tkinter.filedialog import askopenfilename

def main():
    filename = askopenfilename()

    print(filename)

    file = open(filename, 'r')

    print(file.read())

main()