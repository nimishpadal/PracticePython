def checkArmstrong(number):
    strNum = str(number)
    power = (len(strNum))
    sum = 0
    for eachnum in strNum:
        sum += int(eachnum)**power
    if sum == number:
        return True
    else:
        return False

if __name__ =='__main__':
    num = 88593477
    result = (checkArmstrong(num))
    if result:
        print(f"{num} is an armstrong num")
    else:
        print(f"{num} is not an armstrong num ")

