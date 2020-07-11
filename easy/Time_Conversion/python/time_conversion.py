#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    period_unit = s[8:]
    s_converted = s[:8]
    hh = s_converted[:2]

    # https://en.wikipedia.org/wiki/12-hour_clock
    if hh != '12' and period_unit == 'PM':
        hh = str(int(hh) + 12)
    elif hh == '12' and period_unit == 'AM':
        hh = '00'

    s_converted = hh + s_converted[2:]

    return s_converted


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
