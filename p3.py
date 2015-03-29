"""

	Largest prime factor

	Problem 3

	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?

"""

import math

prime_set = {2}


def is_prime(n):
    """
        check if n is a prime number, at a mean while generating a prime list.

    :param n:
    :return:
    """

    # print('try: ',n)
    if n in prime_set:
        return True
    else:
        if n in (0, 1):
            return False

    # print('prime list before try', prime_set)

    # First, search in known prime list
    known_prime_list = sorted(prime_set)
    for p in known_prime_list:
        if n % p == 0:
            return False
    else:
        # Then, try dividing until its root square
        max_try = math.floor(math.sqrt(n))
        while p <= max_try:
            found_next = False
            while not found_next:
                if p == 2:
                    p += 1
                else:
                    p += 2
                if is_prime(p):
                    prime_set.add(p)
                    found_next = True

            if n % p == 0:
                # print('prime list after try', prime_set)
                return False
        else:
            prime_set.add(n)
            # print('prime list after try', prime_set)
            return True


def get_prime_set(max_n):
    res = [is_prime(i) for i in range(2, max_n)]
    print(sorted(prime_set))

def get_next_prime(max_n):
    """
        using a generator to the next prime.

    :param max_n:
    :return:
    """

    for i in range(2,max_n):
        if is_prime(i):
            yield i

def find_max_prime_factor(n):
    max_factor = 1
    half = n // 2
    for i in list(prime_set):
        divide_flag = True
        while divide_flag:
            if n % i == 0:
                n //= i
                if i > max_factor:
                    max_factor = i
            else:
                divide_flag = False
    if is_prime(n):
        if n > max_factor:
            max_factor = n
    return max_factor

def find_max_prime_factor2(n):
    for i in sorted(prime_set, reverse=True):
        if n % i == 0:
            return i

def find_max_prime_factor3(n):
    """
        using generator to find max prime factor.

        This function bases from find_max_prime_factor().
    """

    max_factor = 1
    max_prime_to_try = int(math.sqrt(n))
    tried_prime_list = []

    for i in ( j for j in range(2, max_prime_to_try) if is_prime(j) ):
        print('find in for,', i)
        divide_flag = True
        while divide_flag and n > 1:
            if n % i == 0:
                n //= i
                if i > max_factor:
                    max_factor = i
            else:
                divide_flag = False
        else:
            print('tried',i,', now n=',n ,', max_factor=',max_factor)
            if n == 1:
                break

            if n not in tried_prime_list:   # same number only check once
                tried_prime_list.append(n)
                if is_prime(n):
                    if n>max_factor:
                        max_factor = n
                    break
                else:
                    tmp_max_prime = max(prime_set)
                    if n % tmp_max_prime == 0:
                        n //= tmp_max_prime
                        if tmp_max_prime > max_factor:
                            max_factor = tmp_max_prime
                    ## TODO while checking whether n is a prime, we actually can get its max prime factor, so we can fast-forward i.

    return max_factor

n = 600851475143

def solution1():
    get_prime_set(n // 2)
    print(find_max_prime_factor2(n))

def solution2():
    get_prime_set(int(math.sqrt(n)))
    print(find_max_prime_factor(n))

def solution3():
    print('\nThe max prime factor is : ', find_max_prime_factor3(n))
    # print(sorted(prime_set))

if __name__=='__main__':
    solution3()
