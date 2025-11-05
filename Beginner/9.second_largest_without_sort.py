from typing import List

'''
Problem:
Given a list of integers, find the second largest element without using built-in sorting functions like sort() or sorted().

'''

def second_largest(nums: List[int]) -> int:
    if len(nums) < 2:
        return None
        
    first_largest = float('-inf')
    second_largest = float('-inf')
    
    for num in nums:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 2, 8, 1, 9],
        [1, 1, 1, 1],
        [42]
    ]
    
    for nums in test_cases:
        print(f"Input: {nums}")
        print(f"Second largest: {second_largest(nums)}")
        print()
        
