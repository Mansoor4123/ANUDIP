#Write a function remove_char(s, char) that removes all occurrences of a specific character from a string.
def remove_char(s, char):
    return s.replace(char, '')

s = input("Enter a string: ")
char = input("Enter the character to remove: ")

result = remove_char(s, char)
print("Modified string:", result)
