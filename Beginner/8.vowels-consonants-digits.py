'''
Problem:
Given a string s, count the number of vowels, consonants, digits, and spaces present in it.

'''

def string_info(s: str):
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    for ch in s:
        if ch.isalpha():    
            if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
    return vowels, consonants, digits, spaces

if __name__ == '__main__':
    s = "Hello World 123"
    res = string_info(s)
    print(f"The String {s} contains {res[0]} vowels, {res[1]} consonants, {res[2]} digits, {res[3]} spaces")