'''
Input : geeks_for_geeks Output : GeeksForGeeks
Input : left_index Output : leftIndex
'''

def convertToPascal(str):
    new_str = str.title()
    for x in new_str:
        if x == '_':
            new_str = new_str.replace(x, "")
    return new_str

if __name__ == '__main__':
    str = "geeks_for_geeks"
    print(convertToPascal(str))
