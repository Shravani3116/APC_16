# 11. Find the longest word

file = open("student.txt", "r")

content = file.read()
words = content.split()

longest = max(words, key=len)

print("Longest word:", longest)

file.close()