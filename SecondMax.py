def secondMaxNumber(list):
    max1, max2 = 0,0
    for i in list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    return max2

if __name__ == '__main__':
    nums = [10, 52, 51, 95, 95]
    print(secondMaxNumber(nums))