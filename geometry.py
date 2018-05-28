from z3 import *

circle, square, triangle = Ints('circle square triangle')

s = Solver()

s.add(circle + circle == 10)
s.add(circle*square+square == 12)
s.add(circle*square-triangle*circle==circle)

s.check()

print(s.model())
