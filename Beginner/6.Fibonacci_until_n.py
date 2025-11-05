'''
Problem:
Given a positive integer n, generate and display the Fibonacci sequence up to n terms.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.

The sequence starts as: 0,1,1,2,3,5,8,13,...

'''

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    

if __name__ == '__main__':
    n = 10
    for i in range(n):
        print(f"Fibonacci Series until {n}th term: {fibonacci(i)}")