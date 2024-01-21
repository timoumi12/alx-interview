#!/usr/bin/python3

def minOperations(n):
    '''returns nb of ops if impossible => 0'''

    h = 'H'
    final = 'H'
    l = len(final)
    op = 0
    while(l < n):
        if n % l == 0:
            op += 2
            h = final
            final += final
        else:
            op += 1
            final += h
        l = len(final)
    if len(final) != n:
        return 0
    return op
