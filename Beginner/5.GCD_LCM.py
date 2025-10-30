'''
Problem:
Given two positive integers a and b, compute their Greatest Common Divisor (GCD) and Least Common Multiple (LCM).
You must use the Euclidean Algorithm to find the GCD — not built-in functions like math.gcd() or math.lcm().


Definitions:

GCD (Greatest Common Divisor): The largest positive integer that divides both numbers without leaving a remainder.
LCM (Least Common Multiple): The smallest positive integer that is divisible by both numbers.


(Euclidean Algorithm):

If b == 0, then GCD(a, b) = a.
Otherwise, GCD(a, b) = GCD(b, a % b).
'''

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    return abs(a * b) // GCD(a, b)


if __name__ == '__main__':
    a,b = 20, 30
    print(f"The LCM of {a} and {b} is {LCM(a,b)}")
    print(f"The GCD of {a} and {b} is {GCD(a,b)}")