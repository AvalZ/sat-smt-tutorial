from z3 import *

# SEND + MORE = MONEY

D, E, M, N, O, R, S, Y = Ints('D, E, M, N, O, R, S, Y')

s = Solver()

s.add(Distinct(D, E, M, N, O, R, S, Y))

s.add(And(D>=0, D<=9))
s.add(And(E>=0, E<=9))
s.add(And(M>=0, M<=9))
s.add(And(N>=0, N<=9))
s.add(And(O>=0, O<=9))
s.add(And(R>=0, R<=9))
s.add(And(S>=0, S<=9))
s.add(And(Y>=0, Y<=9))

s.add(1000*S+100*E+10*N+D + 1000*M+100*O+10*R+E == 10000*M+1000*O+100*N+10*E+Y)

print s.check()
print s.model()
