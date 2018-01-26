
class Student(object):
    course_list = []

    def enroll(self, course):
        self.course_list.append(course)


class Course(object):
    pass


itc110 = Course()
itc110.name = "ITC 110"
itc110.room = "BE 1130"
itc110.credits = 5.0

itc220 = Course()
itc220.name = "ITC 220"
itc220.room = "BE 0030"
itc220.credits = 4.0

sally = Student()
sally.name = "Sally Phallon"
sally.SID = 7987979870870

print ("We have a student name: " + sally.name)
print ("Sally's SID is:", sally.SID)
print ("Sally is enrolled in: ")

for course in sally.course_list:
    print ("• " + course.name + ", " + course.room)

sally.enroll(itc110)
sally.enroll(itc220)

print ("Sally is done enrolling.")

for course in sally.course_list:
    print ("• " + course.name + ", " + course.room)

