def factorial(n):
    if (n==0):
        return 1
    else:
        return n * factorial(n-1)

if __name__=='__main__':
    print(f"The factorial of the provided number is {factorial(4)}")