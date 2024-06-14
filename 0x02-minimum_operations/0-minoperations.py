#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Calculates the minimum number of
    operations needed to result in exactly n
    H characters.
    """
    if n < 2:
        return 0
    min_operations = 0
    root = 2
    while root <= n:
        if n % root == 0:
            min_operations += root
            n //= root
            root -= 1
        root += 1
    return min_operations
