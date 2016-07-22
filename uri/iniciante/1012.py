
from math import pow

a, b, c = map( float, raw_input().split())
pi = 3.14159

triangulo = (a * c) / 2.0
circulo = pi * pow(c, 2)
trapezio = ((a + b)/2.0) * c
quadrado = b * b
retangulo = a * b

print "TRIANGULO: %.3f" %(triangulo)
print "CIRCULO: %.3f" %(circulo)
print "TRAPEZIO: %.3f" %(trapezio)
print "QUADRADO: %.3f" %(quadrado)
print "RETANGULO: %.3f" %(retangulo)
