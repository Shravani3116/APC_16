import student

name = input("Enter student name: ")

marks = []
for i in range(5):
    m = float(input("Enter marks: "))
    marks.append(m)

total = student.total_marks(marks)
per = student.percentage(marks)
g = student.grade(per)

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Percentage:", per)
print("Grade:", g)