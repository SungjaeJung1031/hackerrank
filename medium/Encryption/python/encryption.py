#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.


def encryption(s):
    s.replace(" ", "")
    len_s = len(s)
    n_row = round(math.sqrt(len_s))
    n_col = math.ceil(math.sqrt(len_s))

    s_encrypted = [s[i:i+n_col] for i in range(0, len_s, n_col)]
    s_encrypted[-1] = s_encrypted[-1].ljust(n_col)\

    s_encrypted_tr = ""

    for j in range(n_col):
        for i in range(n_row):
            if s_encrypted[i][j] != " ":
                s_encrypted_tr += s_encrypted[i][j]

        s_encrypted_tr += " "

    return s_encrypted_tr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
