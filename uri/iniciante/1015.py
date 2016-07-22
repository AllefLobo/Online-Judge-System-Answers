
from math import sqrt, pow

x1, y1 = map( float, raw_input().split())
x2, y2 = map( float, raw_input().split())

d = sqrt( pow(x2 - x1, 2) + pow( y2 - y1, 2) )

print "%.4f" %(d)
