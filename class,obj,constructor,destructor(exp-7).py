class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")
        print("Student Name:", self.name)
        print("Age:", self.age)

    # Destructor
    def __del__(self):
        print("Destructor called")
        print("Object is destroyed")


# Creating object
s1 = Student("Shravani", 20)

# Deleting object
del s1