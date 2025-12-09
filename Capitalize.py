#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
# def solve(s):
#     for word in s.split():
#         s = s.replace(word, word.capitalize())
#     return s

def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))

# problem with special words
# def solve(s):
#     return s.title()

# def solve(s):
#     result = ""
#     make_cap = True

#     for ch in s:
#         if make_cap and ch.isalpha():
#             result += ch.upper()
#             make_cap = False
#         else:
#             result += ch
#             if ch == " ":
#                 make_cap = True

#     return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
