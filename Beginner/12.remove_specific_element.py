'''
Problem:
Given a list and a target value, remove all occurrences of that target from the list.
The operation should be done without using built-in functions like remove() or list comprehensions.

'''

def remove_all_occurances_of_the_element(nums, element):
    new_nums = []
    for num in nums:
        if num != element:
            new_nums.append(num)
    return new_nums

if __name__ == '__main__':
    nums = [3, 5, 3, 7, 3, 9]
    target = 3
    print(f"The list {nums} after removal of {target} is {remove_all_occurances_of_the_element(nums, target)}")