#!/usr/bin/python3
""" Calculates the fewest number of operations needed,
   to result in exactly n H characters in the file"""


def minOperations(n):
    '''returns nb of ops if impossible => 0'''

    hif n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
