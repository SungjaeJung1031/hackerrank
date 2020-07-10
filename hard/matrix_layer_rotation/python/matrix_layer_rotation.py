#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.


def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0])
    res = [[None]*n for _ in range(m)]
    orig_coords = []

    for c in range(min(m, n)//2):
        coords = []
        for i in range(c, n-c):
            coords.append((c, i))
        for i in range(c+1, m-1-c):
            coords.append((i, n-1-c))
        for i in range(c, n-c)[::-1]:
            coords.append((m-1-c, i))
        for i in range(1+c, m-1-c)[::-1]:
            coords.append((i, c))

        if not coords:
            break

        orig_coords.append(coords)

    rotated_coords = []
    for coords in orig_coords:
        k = r % len(coords)
        rotated_coords.append(coords[k:]+coords[:k])

    for (orig_coord, rotated_coord) in zip(orig_coords, rotated_coords):
        for ((orig_x, orig_y), (rotated_x, rotated_y)) in zip(orig_coord, rotated_coord):
            res[orig_x][orig_y] = matrix[rotated_x][rotated_y]

    print(res)


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
