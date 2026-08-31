# 12. Count frequency of each word

file = open("student.txt", "r")

content = file.read()
words = content.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
print(word_count)

file.close()