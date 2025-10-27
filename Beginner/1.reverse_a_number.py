'''
Problem:
Given an integer n, reverse its digits and return the reversed number.
You must not convert the number into a string or use any string-based operations (like slicing or indexing).

'''

def reverse(n):
    reversed_num = 0
    while n > 0:
        last = n % 10
        reversed_num = reversed_num * 10 + last
        n //= 10

    return reversed_num


if __name__ == '__main__':
    num = int(input("Enter a number to reverse: "))
    print(f"The reversed number is {reverse(num)}")
