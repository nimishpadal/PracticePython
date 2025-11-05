'''
Problem:
Given a list of integers, find the sum of all even numbers and the sum of all odd numbers separately.

'''

def even_odd(nums):
    if len(nums) == 0:
        return 0, 0
    
    even_sum = 0
    odd_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

if __name__ == '__main__':
    nums = [10,4,2,6,3,-7,9,12]
    res = even_odd(nums)
    print(f"The list {nums} has even sum of {res[0]} and odd sum of {res[1]}")
