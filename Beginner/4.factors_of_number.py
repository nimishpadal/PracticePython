'''
Problem:
Given a positive integer n, find and display all factors of n.
A factor of a number is an integer that divides the number completely (i.e., the remainder is 0).

'''
def factors_of_num(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    num = int(input("Enter the number:"))
    print(f"The factors of the number is/are: {factors_of_num(num)}")
