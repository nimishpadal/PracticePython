import random
def listOfLargestNumbers(list,noOfTerms):
    print(f"The input list of numbers is {list}")
    list.sort()
    max_nums = []
    for i in list:
        if i in max_nums:
            continue
        else:
            if len(max_nums) == noOfTerms:
                break
            max_nums.append((list[-1:]))
            list.pop(-1)

    return max_nums

if __name__== '__main__':
       numbers = [random.randint(10,100) for x in range(7)]
       print(listOfLargestNumbers(numbers, 4 ))
       # numbers = [32, 39, 16, 50, 61, 31]
       # numbers.pop(-1)
       # print(numbers)