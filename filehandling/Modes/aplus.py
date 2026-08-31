file = open("Modes.txt", "a+")

file.write("\nMy name is Shravani")

file.seek(0)

print(file.read())

file.close()