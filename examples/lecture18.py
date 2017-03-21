class Person:
    """
    This is a base class representing all people.
    """
    def __init__(self, first_name, last_name, hair_color, eye_color):
        self.first_name = first_name
        self.last_name = last_name
        self.hair_color = hair_color
        self.eye_color = eye_color

    def full_name(self):
        return self.first_name + " " + self.last_name

    def description(self):
        return ("Eye color: " + self.eye_color +
                "\nHair color: " + self.hair_color)

class_list = {
    '3179': {
        'title':'ITC 110',
        'credits': 5,
        'instructor': 'Bob Smith'
    },
    '9876': {
        'title':'WEB 120',
        'credits': 4,
        'instructor': 'Bill Bobbins'
    },
    '0980': {
        'title':'WEB 130',
        'credits': 4,
        'instructor': 'Sally Smith'
    },
}

class Student(Person):
    """
    Student class inherits from Person class.
    """
    def __init__(self, first_name, last_name, hair_color, eye_color):
        super().__init__(first_name, last_name, hair_color, eye_color)
        self.courses = []

    def addCourse(self, course_number):
        self.courses.append(course_number)

    def printCourses(self):
        print(self.full_name() + ' is enrolled in:')
        for course in self.courses:
            print('Course #{0} - {1}'.format(course,
                    class_list[course]['title']))
            print('Credits:', class_list[course]['credits'])
            print('Instructor:', class_list[course]['instructor'])


bob = Person('Bob', 'Billings', 'Brown', 'Purple')
print(bob.full_name())
print(bob.description())

sally = Student('Sally', 'Silly', 'Blue', 'Green')
print(sally.full_name())
print(sally.description())

sally.addCourse('3179')
sally.addCourse('9876')

sally.printCourses()










