# 15. Remove single-line comments

file = open("Q1.py", "r")
output = open("without_comments.py", "w")

for line in file:
    if "#" in line:
        line = line.split("#")[0]

    if line.strip() != "":
        output.write(line)

file.close()
output.close()

print("Comments removed successfully.")