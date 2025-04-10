#Write a function count_char_occurrences(s, char) that counts how many times a specific character char appears in the string s.

def count_char_occurrences(s, char):
    return s.count(char)

s = input("Enter a string: ")
char = input("Enter the character to count: ")

result = count_char_occurrences(s, char)
print(f"The character '{char}' appears {result} times.")
