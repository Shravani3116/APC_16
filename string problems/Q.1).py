#Display the length of string without using length function
# Input a string
text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Length of the string is:", count)