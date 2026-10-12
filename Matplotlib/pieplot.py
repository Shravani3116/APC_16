
import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'C++', 'Cloud']
marks = [85, 75, 90, 80]

plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Pie Plot")
plt.show()
