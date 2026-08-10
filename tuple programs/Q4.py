colors = ("Red","Blue","Black","Yellow","Pink")
color = input("Enter a color to check if it is present in the tuple: ")
if color in colors:
    print(color, "is present in the tuple ")
else:
    print(color, "is not present in tuple ")