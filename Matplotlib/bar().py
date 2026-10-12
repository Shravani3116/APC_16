
import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D', 'E']
marks = [80, 65, 90, 75, 85]

plt.bar(students, marks, color='skyblue')

plt.title("Students Marks - Bar Plot")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
