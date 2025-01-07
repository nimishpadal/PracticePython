def checkSubString(str, substr):
    str = str.lower()
    substr = substr.lower()
    if substr in str:
        return True

if __name__ == '__main__':
    str = "US hit with severe winter storm, six states declare state of emergency"
    substr = "winter storm, six states"
    if (checkSubString(str,substr)):
        print("The String contains the substring")
    else:
        print("Substring not found")