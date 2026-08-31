# 1. Employee Records

def display_employees():
    file = open("employees.txt", "r")

    print("Employee Records:")

    for line in file:
        data = line.strip().split(",")

        emp_id = data[0]
        name = data[1]
        department = data[2]
        salary = float(data[3])

        print(emp_id, name, department, salary)

    file.close()


def highest_paid():
    file = open("employees.txt", "r")

    highest = None

    for line in file:
        data = line.strip().split(",")

        salary = float(data[3])

        if highest is None or salary > highest[3]:
            highest = [data[0], data[1], data[2], salary]

    file.close()

    print("\nHighest Paid Employee:")
    print("ID:", highest[0])
    print("Name:", highest[1])
    print("Department:", highest[2])
    print("Salary:", highest[3])


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")

        total += float(data[3])
        count += 1

    file.close()

    average = total / count

    print("\nAverage Salary:", average)


def above_salary(amount):
    file = open("employees.txt", "r")

    print("\nEmployees earning above", amount, ":")

    for line in file:
        data = line.strip().split(",")

        salary = float(data[3])

        if salary > amount:
            print(data[0], data[1], data[2], salary)

    file.close()

display_employees()
highest_paid()
average_salary()

amount = float(input("\nEnter salary amount: "))
above_salary(amount)