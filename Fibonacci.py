def fibonacci(noOfTerms):
    if (noOfTerms == 0 or noOfTerms == 1):
        return 1
    else:
        return (fibonacci(noOfTerms-1)+fibonacci(noOfTerms-2))


if __name__ == '__main__':
    for i in range(0,10):
        print(fibonacci(i))