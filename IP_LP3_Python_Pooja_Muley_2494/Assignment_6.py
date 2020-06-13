'''Given a matrix of size m*n, m denotes the row starting with index 0 and n denotes the
column starting with index 0.
The matrix will hold distinct integers as elements.
We need to find a distinct number of positional elements which are either the minimum
or maximum in their corresponding row or column.
Please return -1 if any row or any column has multiple minimum or maximum
elements.
For example, given a matrix of size 3*3, the elements are stored as follows.
1 3 4
5 2 9
8 7 6
The expected output is 7.'''



import math
import os
import random
import re
import sys


# Complete the countSpecialElements function below.

def countSpecialElements(matrix):
    nRows = len(matrix)
    nCount = 0

    for row in matrix:
        for indexCol, element in enumerate(row):

            if element == min(row) or element == max(row):
                if row.count(element) > 1:
                    return -1
                nCount = nCount + 1

            else:
                listColumn = []

                for indexRow in range(0, nRows):
                    listColumn.append(matrix[indexRow][indexCol])

                if element == min(listColumn) or element == max(listColumn):
                    if listColumn.count(element) > 1:
                        return -1
                    nCount = nCount + 1

    return nCount


if __name__ == '__main__':
    nCount = countSpecialElements([[1, 3, 4], [5, 2, 9], [8, 7, 6]])
    print(nCount)