
from math import pow

a, b, c = map( float, raw_input().split() )

if a + b > c and b + c > a and a + c > b:
    print "Perimetro = %.1f" %(a + b + c)
else:
    print "Area = %.1f" %( ((a+b)/2.0) * c )
