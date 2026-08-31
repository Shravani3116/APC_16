# 17. Student records

file = open("students.txt", "r")

records = []
file.readline()

for line in file:
    data = line.strip().split(",")

    roll_no = data[0]
    name = data[1]
    marks = int(data[2])

    records.append([roll_no, name, marks])

file.close()

print("All Student Records:")

for record in records:
    print(record[0], record[1], record[2])

highest = records[0]

for record in records:
    if record[2] > highest[2]:
        highest = record

print("\nStudent with highest marks:")
print("Roll No:", highest[0])
print("Name:", highest[1])
print("Marks:", highest[2])

total = 0

for record in records:
    total += record[2]

average = total / len(records)

print("\nAverage Marks:", average)

print("\nStudents who scored more than 80:")

for record in records:
    if record[2] > 80:
        print(record[0], record[1], record[2])