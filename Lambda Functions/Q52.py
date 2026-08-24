words = [
    "Python",
    "Java",
    "Programming",
    "Computer",
    "AI",
    "Development",
    "Code"
]


word_lengths = list(
    map(lambda word: (word, len(word)), words)
)

print("Length of every word:")
print(word_lengths)


long_words = list(
    filter(lambda word: len(word) > 5, words)
)

print("\nWords having more than five characters:")
print(long_words)

sorted_words = sorted(
    words,
    key=lambda word: len(word)
)

print("\nWords sorted according to length:")
print(sorted_words)