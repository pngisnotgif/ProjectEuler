"""
    Problem 1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

a = range(3,1000,3)
b = range(5,1000,5)
c = range(3*5, 1000, 3*5)
sum_3_5 = sum(a) + sum(b) - sum(c)

print(sum_3_5)    
