from z3 import *


x = BitVec('x', 32)
y = BitVec('y', 32)


trick = (x ^ y) < 0

opposite = Or(And(x < 0, y >= 0), And(x >= 0, y < 0))

prove(trick == opposite)
