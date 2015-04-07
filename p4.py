__author__ = 'matthew'

"""
    Problem 4

    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

max_product = 99 * 99
max_a = 99
max_b = 99
for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        product = i * j
        str_p = str(product)
        len_p = len(str_p)
        is_palindromic = True
        for t in range(0, int(len_p/2)):
            if str_p[t] != str_p[-t-1]:
                is_palindromic = False
                break
        else:
            if product > max_product:
                max_product = product
                max_a = i
                max_b = j

print(max_product, " = ", max_a, "*", max_b)
