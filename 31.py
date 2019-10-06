import re
import math


def simplify(n):
    return math.sqrt(n)


# def desimplify(s):
#     a = s
#     s = [int(i) for i in s.split() if i.isdigit()]
#     if len(s) == 1 and re.match(r'sqrt', a):
#         return s[0]
#     if len(s) == 1:
#         return pow(s[0], 2)
#     return pow(s[0], 2)*s[1]


# print(desimplify("2"))
print(simplify(4))
