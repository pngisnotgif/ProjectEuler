__author__ = 'matthew'
"""
    Problem 5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


"""

'''
    2
    3
    4 = 2*2
    5
    6 = 2 * 3
    7
    8 = 2**3
    9 = 3*3
    10 = 2 * 5

    11              choose 11
    12 = 2*2 * 3
    13              choose 13
    14 = 2 * 7      choose 7
    15 = 3 * 5      choose 5
    16 = 2**4       choose 2**4
    17              choose 17
    18 = 2* 3*3     choose 3*3
    19              choose 19
    20 = 2*2 * 5
'''

res = 2**4*3*3*5*7*11*13*17*19
print(res)