import numpy as np

def splitArray(arr,split):
    # Input: [10 25 40 55 70 85]
    # Output: [40 55 70 85 10 25]
    firstPart = list(map(int, arr[split:]))
    secondPart = list(map(int, arr[:split]))
    return firstPart + secondPart
if __name__ == '__main__':
    arr = np.arange(10,100,15)
    # print(arr[:2] + arr[2:])
    print(splitArray(arr, 2))


