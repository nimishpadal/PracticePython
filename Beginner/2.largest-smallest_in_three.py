'''
Problem:
Given three numbers, determine which one is the largest and which one is the smallest.
You must solve this using conditional statements — not using built-in functions like max() or min().
'''

def largest_and_smallest(num1, num2, num3):
    # Find largest
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    else:
        largest = num3
    
    # Find smallest
    if num1 < num2 and num1 < num3:
        smallest = num1
    elif num2 < num1 and num2 < num3:
        smallest = num2
    else:
        smallest = num3
    return largest, smallest

if __name__ == '__main__':
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    result = largest_and_smallest(num1, num2, num3)
    print(f"Amongst the numbers entered, the largest is {result[0]} and smallest is {result[1]}")