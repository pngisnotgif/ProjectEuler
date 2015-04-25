__author__ = 'matthew'

"""
   Problem 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

"""
    (1+2+...+n)^2 - (1^2+2^2+...+n^2)
= 2 * [1*2+1*3+...+1*n + 2*3+2*4+...+2*n + ... + (n-1)*n ]
= 2 *[ (2+3+...+n) + 2*(3+4+...+n) + ... + (n-1)*n ]
= 2 * { (2+n)*(n-1)/2 + 2*(3+n)*(n-2)/2 + ... + (n-1)*[(n+n)*1/2] }
= (2+n)*(n-1) + 2*(3+n)*(n-2) + ... + (n-1)*[(n+n)*1]

"""

n = 100
res = 0
for i in range(1,n):
    a = (1 + i) + n
    b = n - i
    product = i * a * b
    res += product

print(res)
