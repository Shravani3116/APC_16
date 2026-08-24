def check_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False
char = input("Enter a character: ")    
if check_vowel(char):
    print(char, "is a vowel.")
else:
    print(char, "is not a vowel.")
