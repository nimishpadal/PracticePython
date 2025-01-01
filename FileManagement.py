import os.path
from pathlib import Path
directory = Path("D:\\AutomationScript")

def checkItems():
    items =[]
    if directory.exists() and directory.is_dir():
        # print(f"The items in {directory} are: ")
        for item in directory.iterdir():
            items.append(item.name)
    else:
        print(f"The directory '{directory}' does not exist or is not a directory.")
    return items

def createItem(file_name):
    full_path = os.path.join(directory, file_name)
    try:
        with open(full_path, "w") as file_name:
            file_name.write("content")
            print(f"file created under {file_name.name}")
    except:
        print("error occured")

if __name__ == '__main__':
    if len(checkItems()) == 3:
        createItem("test4.txt")
    else:
        print("The files already exist")
