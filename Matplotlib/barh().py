
import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'C++', 'Cloud', 'DBMS']
marks = [85, 70, 90, 80, 75]

plt.barh(subjects, marks, color='orange')

plt.title("Subject Marks - Horizontal Bar Plot")
plt.xlabel("Marks")
plt.ylabel("Subjects")

plt.show()
