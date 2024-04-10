
import math
import os
import random
import re
import sys


def solve(s):
    ans = (i.capitalize() for i in s.split(' ')) #generate expression
    return ' '.join(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()