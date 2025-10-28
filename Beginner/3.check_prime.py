'''
Problem:
Given an integer n, determine whether it is a prime number or not.
A number is said to be prime if it is greater than 1 and divisible only by 1 and itself.

'''

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    print('-----------------------------------')
    print("Check if the number is prime!")
    num = int(input("Enter the number:"))
    if check_prime(num):
        print("Yes!, its a prime number")
    else:
        print("No its not a prime")