#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    
    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(1, i):
                left = triangle[i - 1][j - 1]
                right = triangle[i - 1][j]
                row.append(left + right)
            row.append(1)
        triangle.append(row)

    return triangle
