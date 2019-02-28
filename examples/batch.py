from tkinter.filedialog import askopenfilename, asksaveasfilename

from usernamer import usernamer

print("Batch process usernames....")

student_db_file = askopenfilename()
username_db_file = asksaveasfilename()
print("Student File: ", student_db_file)
print("Save as File: ", username_db_file)
student_db = open(student_db_file, "r")
username_db = open(username_db_file, "w")

for line in student_db:
    first_name, last_name = line.split()
    uname = usernamer(first_name, last_name)
    print(uname, file=username_db)

student_db.close()
username_db.close()

print("Done processing.")
