__author__ = 'matthew'

"""
    Problem 7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?

"""

from p3 import is_prime

def get_Nth_prime(n):
    if n==1:
        return 2

    i = 1
    next_prime = 1  # for start of while

    while i<n:
        next_prime += 2
        if is_prime(next_prime):
            i+=1

    return next_prime

if __name__=="__main__":
    #for i in range(1,7):
    print(get_Nth_prime(10001))