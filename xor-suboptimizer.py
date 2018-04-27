#!/usr/bin/python

"""
x^y == (((y & x)*-2) + (y + x))
"""
from z3 import *

x = BitVec('x', 32)
y = BitVec('y', 32)
output = BitVec('output', 32)

s = Solver()
s.add(x^y == output)
s.add(((y & x) * 0xFFFFFFFE) + (y + x) != output)
print s.check()
