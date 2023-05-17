#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_row = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] ** 2)
        new_matrix.append(new_row)
        new_row = []
    return (new_matrix)
