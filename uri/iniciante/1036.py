
from math import sqrt, pow

a, b, c = map( float, raw_input().split() )
delta = pow(b,2) - 4*a*c
if delta == 0:
    print "Impossivel calcular"
else:
    r1 = (b*(-1) + sqrt(delta) )/ 2.0 * a
    r2 = (b*(-1) - sqrt(delta) )/ 2.0 * a

    print "R1 = %.5f" %(r1)
    print "R2 = %.5f" %(r2)
