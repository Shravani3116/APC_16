# 1. Create a file and write student information

file = open("student.txt", "w")

file.write("Name: Shravani\n")
file.write("Roll Number: 16\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semester: 5th\n")

file.close()

print("Student information written successfully.")