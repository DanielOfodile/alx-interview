#!/usr/bin/python3

def pascal_triangle(n:int)->List[List[int]]:
    """
    A function that generates Pascal's triangle of n
    :param n: an integer, the number of rows of Pascal's triangle.
    :return: If n>0, returns a list of lists of integers representing the Pascal's triangle of n
    If n<=0, returns an empty list
    """
    if n<=0:
        return []
    else:
        triangle = []
        for i in range(n):
            row = [1]*(i+1)  # Create a row of 1s
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

# Example usage
print(pascal_triangle(5))
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

