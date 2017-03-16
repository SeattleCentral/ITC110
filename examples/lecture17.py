class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def make_student(data_row):
    # Take a row of data from the students.csv file and
    # return a new Student object
    last_name, first_name, hours, qpoints = data_row.split(',')
    name = first_name + " " + last_name
    return Student(name, hours, qpoints)

def main():
    filename = 'students.csv'
    file = open(filename, 'r')

    best_student = make_student(file.readline())

    for line in file.readlines():
        student = make_student(line)

        if student.gpa() > best_student.gpa():
            best_student = student

    file.close()

    print("The best student is: ", best_student.getName())
    print("Hours: ", best_student.getHours())
    print("GPA: ", best_student.gpa())


if __name__ == '__main__':
    main()
































