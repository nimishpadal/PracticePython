def printPrimeNumbers(start,stop):
    primes = []
    for i in range(start, stop):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes


if __name__ == '__main__':
    print(printPrimeNumbers(2, 20))