
n = int(input())
print n
cedulas = dict()
cedula = [100, 50, 20, 10, 5, 2, 1]
cont = 0

for x in cedula:
    while x <= n:
        n = n - x
        cont = cont + 1
    cedulas[x] = cont
    cont = 0

print "%d nota(s) de R$ %d,00" %( cedulas[100], 100)
print "%d nota(s) de R$ %d,00" %( cedulas[50], 50)
print "%d nota(s) de R$ %d,00" %( cedulas[20], 20)
print "%d nota(s) de R$ %d,00" %( cedulas[10], 10)
print "%d nota(s) de R$ %d,00" %( cedulas[5], 5)
print "%d nota(s) de R$ %d,00" %( cedulas[2], 2)
print "%d nota(s) de R$ %d,00" %( cedulas[1], 1)
