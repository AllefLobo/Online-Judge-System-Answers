
from math import sqrt, pow

a, b, c = map( float, raw_input().split() )

if a == 0 or b == 0 or c == 0:
    print "Impossivel calcular"
else:
    r1 = ( (b *(-1)) + sqrt( pow(b, 2) - (4 * a * c) ))/ 2.0 * a
    r2 = ( (b*(-1)) - sqrt( pow(b,2) - (4 * a * c) ))/ 2.0 * a

    print "R1 = %.5f" %(r1)
    print "R2 = %.5f" %(r2)
