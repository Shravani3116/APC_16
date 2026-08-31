from student.details import student_details
from student.marks import student_marks
from faculty.details import faculty_details

student_name, roll = student_details()
total = student_marks()

faculty_name, subject = faculty_details()

print("\n--- College Information ---")
print("Student Name:", student_name)
print("Roll Number:", roll)
print("Total Marks:", total)

print("\nFaculty Name:", faculty_name)
print("Subject:", subject)