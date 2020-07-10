#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.


def organizingContainers(container):
    cnt_type = [sum(n_type_balls) for n_type_balls in zip(*container)]
    cnt_container = [sum(n_balls) for n_balls in container]

    cnt_type.sort()
    cnt_container.sort()

    return "Possible" if cnt_type == cnt_container else "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
