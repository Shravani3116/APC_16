# 16. Convert text to uppercase

file = open("student.txt", "r")
output = open("uppercase.txt", "w")

content = file.read()

output.write(content.upper())

file.close()
output.close()

print("Uppercase file created successfully.")