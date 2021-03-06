import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(string):
    full_name = string.split(' ')
    return ' '.join((word.capitalize() for word in full_name))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()