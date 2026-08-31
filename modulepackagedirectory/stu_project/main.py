from student.marks import total, percentage
from student.grade import calculate_grade
from student.attendance import eligibility

name = input("Enter student name: ")

marks = []
for i in range(5):
    marks.append(float(input("Enter marks: ")))

attended = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes: "))

t = total(marks)
p = percentage(marks)
g = calculate_grade(p)
e = eligibility(attended, total_classes)

print("\n--- Student Report ---")
print("Name:", name)
print("Total Marks:", t)
print("Percentage:", p)
print("Grade:", g)
print("Attendance:", (attended / total_classes) * 100, "%")
print("Eligibility:", e)