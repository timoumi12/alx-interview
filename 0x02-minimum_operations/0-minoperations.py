#!/usr/bin/python3
""" Calculates the fewest number of operations needed,
   to result in exactly n H characters in the file"""


def minOperations(n):
    '''returns nb of ops if impossible => 0'''

    h = 'H'
    final = 'H'
    op = 0
    while(len(final) < n):
        if n % len(final) == 0:
            op += 2
            h = final
            final += final
        else:
            op += 1
            final += h
    if len(final) != n:
        return 0
    return op
