# 8. Display lines in reverse order

file = open("student.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line, end="")

file.close()