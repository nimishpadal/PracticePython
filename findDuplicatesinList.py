def findDuplicates(nums):
    duplicates = []
    for i in nums:
        if (nums.count(i)>1 and i not in duplicates):
            duplicates.append(i)
    return duplicates

if __name__ == '__main__':
    nums = [1,1,2,3,4,4,5,8,9,11,12,11]
    print(findDuplicates(nums))