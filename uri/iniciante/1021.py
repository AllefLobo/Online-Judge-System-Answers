
n = float(input())
cedulas = dict()
cedula = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
cont = 0

for x in cedula:
    while x <= n:
        n = n - x
        cont = cont + 1
    cedulas[x] = cont
    cont = 0

print "NOTAS:"
print "%d nota(s) de R$ %.2f" %( cedulas[100], 100)
print "%d nota(s) de R$ %.2f" %( cedulas[50], 50)
print "%d nota(s) de R$ %.2f" %( cedulas[20], 20)
print "%d nota(s) de R$ %.2f" %( cedulas[10], 10)
print "%d nota(s) de R$ %.2f" %( cedulas[5], 5)
print "%d nota(s) de R$ %.2f" %( cedulas[2], 2)
print "MOEDAS:"
print "%d moeda(s) de R$ %.2f" %( cedulas[1], 1)
print "%d moeda(s) de R$ %.2f" %( cedulas[0.50], 0.50)
print "%d moeda(s) de R$ %.2f" %( cedulas[0.25], 0.25)
print "%d moeda(s) de R$ %.2f" %( cedulas[0.10], 0.10)
print "%d moeda(s) de R$ %.2f" %( cedulas[0.05], 0.05)
print "%d moeda(s) de R$ %.2f" %( cedulas[0.01], 0.01)
