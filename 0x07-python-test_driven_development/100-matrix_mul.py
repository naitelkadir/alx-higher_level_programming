#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """define a function that return prod of two matrix"""
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    for row in m_a:
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = [[0] * len(m_b[0]) for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b)):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix

