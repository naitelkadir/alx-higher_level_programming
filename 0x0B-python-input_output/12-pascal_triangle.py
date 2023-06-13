#!/usr/bin/python3
"""define a function that returns a list"""

def pascal_triangle(n):
    """a function that returns a pascal triangle"""
    
    if n <= 0:
        return ([])
    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        new = [1]
        for i in range(len(triangle) - 1):
            new.append(triangle[i] + triangle[i + 1])
        new.append(1)
        triangles.append(new)
    return (triangles) 
