# CPE 101-01
# LAB 6
# Name: Tyler Baxter
# Section: 03

# This function returns a string with the vowels
def vowel_extractor(s1: str) -> str:
    s2 = ""
    vowels = "AaEeIiOoUu"
    for char in s1:
        if char in vowels:
            s2 += char
    return s2


# This function returns a same string with every word starting with uppercase
def str_capitalize(s1: str) -> str:
    s2 = ""
    word_start = False
    phrase_start = True
    for char in s1:
        if phrase_start:
            s2 += chr(ord(s1[0]) - 32)
            phrase_start = False
        elif char == " ":
            word_start = True
            s2 += char
        elif 65 <= ord(char) <= 90 and word_start:
            s2 += char
            word_start = False
        elif word_start:
            s2 += chr(ord(char) - 32)
            word_start = False
        elif 65 <= ord(char) <= 90:
            s2 += chr(ord(char) + 32)

        else:
            s2 += char
    return s2


# This function takes a string as input and return the ROT-13 encoding of the given characters
def str_rotate(s1: str) -> str:
    s2 = ""
    for char in s1:
        if char.isalnum():
            if 65 <= ord(char) <= 77:
                s2 += chr(ord(char) + 13)
            if 78 <= ord(char) <= 90:
                s2 += chr(ord(char) - 13)
            if 97 <= ord(char) <= 109:
                s2 += chr(ord(char) + 13)
            if 110 <= ord(char) <= 122:
                s2 += chr(ord(char) - 13)
        else:
            s2 += char
    return s2


# This function returns a substring that begins from start index and ends at stop index and increasing step characters
def make_substring(s1: str, start: int, end: int, i: int) -> str:
    s2 = ""
    for idx in range(start, end, i):
        s2 += s1[idx]
    return s2


# This function takes a string as input and returns True if string is palindrome
def is_palindrome(s1: str) -> bool:
    s21 = ""
    s22 = ""
    if len(s1) % 2 == 0:
        center = int(len(s1) / 2)
        for idx in range(0, center, 1):
            s21 += s1[idx]
        for idx in range(center, len(s1), 1):
            s22 = s1[idx] + s22
    else:
        center = int((len(s1) + 1) / 2)
        for idx in range(0, center - 1, 1):
            s21 += s1[idx]
        for idx in range(center, len(s1), 1):
            s22 = s1[idx] + s22
    return s21 == s22


# This function takes a string and a character, returns how many times the character was repeated in the string
def count_characters(s1: str, char: str) -> int:
    s1.lower()
    char.lower()
    if not (char in s1):
        return -1
    else:
        counter = 0
        for idx in range(len(s1)):
            if s1[idx] == char:
                counter += 1
    return counter
